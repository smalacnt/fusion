"""fusion is the app entry"""
from flask import Flask, request, jsonify
from fusion.api import ifcdta, util
from fusion.flask.exception_handle import InvalidUsage

APP = Flask(__name__)
LOG = APP.logger

@APP.route('/')
def index():
    """index return the index page """
    return 'Welcome come to Fusion'

@APP.route('/api/ifc', methods=['POST', 'GET'])
def interface():
    """add or get interface """
    LOG.debug(request)
    if request.method == 'POST':
        ifc = request.get_json()
        name = ifc['name']
        fields = ifc['fields']
        ifcdta.addifc(name, fields)
        return 'OK'
    else:
        name = request.args.get('name')
        ifc = ifcdta.getifc(name)
        return ifc

@APP.route('/dbtime', methods=['GET'])
def dbtime():
    """return mysql database time """
    return '%s' % util.get_dbtime()

@APP.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    """handle exception and return 400 with exception message """
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@APP.errorhandler(Exception)
def handle_exception(exception):
    """handle exception """
    msg = dict()
    msg['message'] = '%s' % exception
    response = jsonify(msg)
    response.status_code = 500 #Internal Server Error
    return response
