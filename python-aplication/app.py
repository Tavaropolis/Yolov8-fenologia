from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import cv2
import base64
import re

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET', 'POST'])
def home_path():
    return "Página inicial da API de Yolov8 aplicado a fenologia", 200

@app.route('/sobre', methods=['GET', 'POST'])
def about_path():
    return "Projeto desenvolvido como TCC do curso de Análise e Desenvolvimento de Sistemas pelo Instituto Federal de SP - Campus Capivari", 200

@app.route('/api/imagetopython', methods=["POST"])
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
        # cv2_img = cv2.polylines(img=cv2_img, pts=np.int32([points]), isClosed=True, color=(0, 0, 255), thickness=2)

        #Desenhando o retangulo com as informações
        # cv2_img = cv2.rectangle(img=cv2_img, pt1=(image_width - int(image_width - (image_width * 0.80)), 0), pt2=(image_width, int(image_height - (image_height * 0.95))), color=(255, 255, 255), thickness=-1)

        # cv2_img = cv2.putText(img=cv2_img, text=f"conf: {image_confidence}", org=(image_width - int(image_width - (image_width * 0.80)), int(image_height - (image_height * 0.98))), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.8, color=(0, 0, 0), thickness=2, lineType=cv2.LINE_AA, bottomLeftOrigin=False)
    except:
        return "Erro na plotagem da copa", 500

    #Criando a máscara
    try:
        mask = np.zeros(shape=(image_height, image_width), dtype=np.uint8) #Aplica preto na foto inteira
        treetop_mask = cv2.fillPoly(img=mask, pts=np.int32([points]), color=255) #Cria a máscara da copa
        cv2_img_mask = cv2.bitwise_and(src1=treetop_mask, src2=treetop_mask, mask=mask)
        
        reverse_mask = cv2.bitwise_not(cv2_img_mask)
        cv2_img_reserve = cv2.bitwise_and(cv2_img_orignal, cv2_img_orignal, mask=treetop_mask)
    except:
        return "Erro na montagem da máscara", 500

    #Analisando a intensidade foliar
    try:
        hsv_img = cv2.cvtColor(cv2_img_reserve,  cv2.COLOR_BGR2HSV)
        lower_hsv = np.array([0, 51, 0]) #Tons fortes de verde
        upper_hsv = np.array([204, 255, 204]) #Tons fracos de verde

        mask = cv2.inRange(hsv_img, lower_hsv, upper_hsv)
        detected_img = cv2.bitwise_and(cv2_img_reserve, cv2_img_reserve, mask=mask) #Detectando apenas o verde na foto
    except:
        return "Erro ao calcular intensidade foliar", 500
    
    # Imagem para Base64  
    try:
        _, im_arr = cv2.imencode(f'.{file_extension}', detected_img)  # im_arr: image in Numpy one-dim array format.
        im_bytes = im_arr.tobytes()
        im_b64 = base64.b64encode(im_bytes).decode('utf-8')

        return jsonify({
            "result": "Hello My Dear",
            "imageBase64": f"{image_prefix},{im_b64}"
        }), 200
    except: 
        return "Erro na reconversão da imagem", 500
