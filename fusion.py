from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome come to Fusion'

@app.route('/hello/<name>')
def hello(name=None):
    if name == None:
        name = 'world'
    return 'Hello, %s!' % name
