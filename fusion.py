from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome come to Fusion'

@app.route('/hello/<name>')
def hello(name=None):
    if name == None:
        name = 'world'
    return 'Hello, %s!' % name

@app.route('/interface', methods=['POST', 'GET', 'PUT', 'DELETE'])
def interface():
    app.logger.debug(request.get_json())
    if request.method == 'POST':
        json = request.get_json()
        return json['name']
    elif request.method == 'GET':
        return 'GET'
    elif request.method == 'PUT':
        return 'PUT'
    elif request.method == 'DELETE':
        return 'DELETE'
