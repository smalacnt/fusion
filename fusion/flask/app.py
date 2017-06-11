"""fusion is the app entry"""
from flask import Flask, request, jsonify
from fusion.api import ifcdta, util
from fusion.flask.exception import InvalidUsage

app = Flask(__name__)
logger = app.logger

@app.route('/')
def index():
    """index return the index page """
    return 'Welcome come to Fusion'

@app.route('/api/dbtime', methods=['GET'])
def dbtime():
    """return databse time"""
    resp = dict()
    resp['time'] = str(util.get_dbtime())
    return jsonify(resp)

@app.route('/api/ifc', methods=['POST', 'GET'])
def interface():
    """add or get interface """
    logger.debug(request)
    if request.method == 'POST':
        ifc = request.get_json()
        name = ifc['name']
        fields = ifc['fields']
        msg = ifcdta.addifc(name, fields)
        return jsonify(msg)
    else:
        name = request.args.get('name')
        ifc = ifcdta.getifc(name)
        return jsonify(ifc)

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    """handle exception and return 400 with exception message """
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.errorhandler(Exception)
def handle_exception(exception):
    """handle exception """
    msg = dict()
    msg['message'] = str(exception)
    response = jsonify(msg)
    response.status_code = 500 #Internal Server Error
    return response
