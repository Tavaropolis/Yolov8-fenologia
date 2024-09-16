from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return "Bão dia so"
    else:
        return "Hello, World!"

@app.route('/name/<string:myname>')
def show_name(myname):
    return f"Seu nome é {myname}"

@app.route('/add/<int:number>/<int:number2>')
def add(number: int, number2: int):
    return f"A soma dos números é {number + number2}"

