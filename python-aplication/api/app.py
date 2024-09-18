from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import numpy as np
import cv2

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return "Bão dia so"
    else:
        return "Hello, World!"

@app.route('/name/<string:myname>')
def show_name(myname):
    return f"Seu nome é {myname}"

@app.route('/imagetopython', methods=["POST"])
def image_to_python():
    data = request.get_json()

    # Base64 para Imagem
    image_string = data['image']
    image_prefix = image_string.split(',')[0] #Pega o prefixo do base64
    image_string = image_string.split(',')[1] #Pega o corpo do base64
    image_string = base64.b64decode(image_string)
    np_array = np.frombuffer(image_string, dtype=np.uint8)
    cv2_img = cv2.imdecode(np_array, flags=cv2.IMREAD_COLOR)

    #Alterando a imagem de entrada
    cv2_img = cv2_img[0:244, 0:244]

    # Imagem para Base64  
    _, im_arr = cv2.imencode('.webp', cv2_img)  # im_arr: image in Numpy one-dim array format.
    im_bytes = im_arr.tobytes()
    im_b64 = base64.b64encode(im_bytes).decode('utf-8')

    return jsonify({
        "result": "Hello My Dear",
        "imageBase64": f"{image_prefix},{im_b64}"
    })

