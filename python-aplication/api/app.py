from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import cv2
import base64
import re

app = Flask(__name__)
cors = CORS(app, resources={r'/*': {'origins': 'https://yolov8-fenologia.vercel.app'}})

@app.route("/", methods=['GET', 'POST'])
def home_path():
    return "Página inicial da API de Yolov8 aplicado a fenologia", 200

@app.route('/sobre', methods=['GET', 'POST'])
def about_path():
    return "Projeto desenvolvido como TCC do curso de Análise e Desenvolvimento de Sistemas pelo Instituto Federal de SP - Campus Capivari", 200

@app.route('/imagetopython', methods=["POST"])
def image_to_python():
    data = request.get_json()

    # Base64 para Imagem
    try:
        image_string = data['image']
        image_prefix = image_string.split(',')[0] #Pega o prefixo do base64
        image_string = image_string.split(',')[1] #Pega o corpo do base64
        image_string = base64.b64decode(image_string)
        file_extension = re.findall("png|jpg|jpeg|webp", image_prefix)[0]
        np_array = np.frombuffer(image_string, dtype=np.uint8)
        cv2_img = cv2_img_orignal = cv2_img_mask = cv2.imdecode(np_array, flags=cv2.IMREAD_COLOR)
    except:
        return "Erro na conversão da imagem", 500

    #Alterando a imagem de entrada
    try: 
        image_points = data['predictions']
        image_width, image_height = data['width'], data['height']
        image_confidence = data['confidence']

        #Desenhando a copa da árvore
        points = np.array(image_points)
        cv2_img = cv2.polylines(img=cv2_img, pts=np.int32([points]), isClosed=True, color=(0, 0, 255), thickness=2)
    except:
        return "Erro na plotagem da copa", 500

    #Criando a máscara
    try:
        dark_mask = np.zeros(shape=(image_height, image_width), dtype=np.uint8) #Aplica preto na foto inteira
        treetop_mask = cv2.fillPoly(img=dark_mask, pts=np.int32([points]), color=255) #Cria a máscara da copa
        
        cv2_img_mask = cv2.bitwise_and(cv2_img_orignal, cv2_img_orignal, mask=treetop_mask) #Junta os dois
    except:
        return "Erro na montagem da máscara", 500

    #Analisando a intensidade foliar
    try:
        hsv_img = cv2.cvtColor(cv2_img_mask,  cv2.COLOR_BGR2HSV) #Transforma imagem em HSV
        lower_hsv = np.array([35, 10, 10]) #Tons fortes de verde
        upper_hsv = np.array([90, 255, 255]) #Tons fracos de verde

        green_mask = cv2.inRange(hsv_img, lower_hsv, upper_hsv)
        leaf_index = (round(np.count_nonzero(green_mask) / np.count_nonzero(treetop_mask) * 100, 1)) #Calcula intensidade foliar
    except:
        return "Erro ao calcular intensidade foliar", 500
    
    # Imagem para Base64  
    try:
        _, im_arr = cv2.imencode(f'.{file_extension}', cv2_img)  # im_arr: image in Numpy one-dim array format.
        im_bytes = im_arr.tobytes()
        im_b64 = base64.b64encode(im_bytes).decode('utf-8')

        return jsonify({
            "imageBase64": f"{image_prefix},{im_b64}",
            "confidence": image_confidence,
            "leaf_index" : leaf_index
        }), 200
    except: 
        return "Erro na reconversão da imagem", 500

if __name__ == '__main__':
    app.run(debug=True)