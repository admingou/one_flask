from . import APIException

class Success(APIException):
    code = 200
    msg = ""
    status_code = 2000


class Error(APIException):
    code = 200
    msg = ""
    status_code = 2001