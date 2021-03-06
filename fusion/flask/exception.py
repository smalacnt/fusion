# -*- coding: utf-8 -*-
"""module exception hander """
class InvalidUsage(Exception):
    """"exception handler class """
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        """method implementation """
        resp = dict(self.payload or ())
        resp['message'] = self.message
        return resp
