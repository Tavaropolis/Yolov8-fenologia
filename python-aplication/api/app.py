from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import numpy as np
import cv2

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
        np_array = np.frombuffer(image_string, dtype=np.uint8)
        cv2_img = cv2.imdecode(np_array, flags=cv2.IMREAD_COLOR)
    except:
        return "Erro na conversão da imagem", 500

    #Alterando a imagem de entrada
    try: 
        image_points = data['predictions']
        image_width = data['width']
        image_height = data['height']
        image_confidence = data['confidence']

        #Desenhando a copa da árvore
        points = np.array(image_points)
        cv2_img = cv2.polylines(img=cv2_img, pts=np.int32([points]), isClosed=True, color=(0, 0, 255), thickness=2)

        #Desenhando o retangulo com as informações
        cv2_img = cv2.rectangle(img=cv2_img, pt1=(image_width - int(image_width - (image_width * 0.80)), 0), pt2=(image_width, int(image_height - (image_height * 0.95))), color=(255, 255, 255), thickness=-1)

        cv2_img = cv2.putText(img=cv2_img, text=f"conf: {image_confidence}", org=(image_width - int(image_width - (image_width * 0.80)), int(image_height - (image_height * 0.98))), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.8, color=(0, 0, 0), thickness=2, lineType=cv2.LINE_AA, bottomLeftOrigin=False)
    except:
        return "Erro na plotagem da copa", 500

    # Imagem para Base64  
    try:
        _, im_arr = cv2.imencode('.webp', cv2_img)  # im_arr: image in Numpy one-dim array format.
        im_bytes = im_arr.tobytes()
        im_b64 = base64.b64encode(im_bytes).decode('utf-8')

        return jsonify({
            "result": "Hello My Dear",
            "imageBase64": f"{image_prefix},{im_b64}"
        }), 200
    except: 
        return "Erro na reconversão da imagem", 500
