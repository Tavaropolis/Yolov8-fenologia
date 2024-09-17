from flask import Flask, request, jsonify
from flask_cors import CORS
import base64

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

    image = base64.base64decode(data['image'])
    image = base64.base64encode(image)

    return jsonify({
        "result": "Hello My Dear",
        "imageBase64": image
    })

