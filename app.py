# -*- coding: UTF-8 -*-
from flask  import  Flask, request
from one_all_web.home import home
from one_all_web.api import api
from werkzeug.exceptions import HTTPException
from one_all_web.error import APIException
from one_all_web.error.isweb import is_web_or_api
from one_all_web.error.web_error import web_errors
from flask_cors import *
from one_all_web.config import config
from one_all_web.models import AccProject,User,YunPan
from  one_all_web.models.base_model import db


app = Flask(__name__)
CORS(app, supports_credentials=True)
app.register_blueprint(home)
app.register_blueprint(api, url_prefix="/api")
app.config.from_object(config)
db.init_app(app)
db.create_all(app=app)






@app.errorhandler(Exception)
def  framework_error(e):
    """
    异常种类:APIException,
    HTTPException,
    Exception
    :param e:
    :return:
    """
    if is_web_or_api():
        if    isinstance(e,APIException):
              return  e
        if    isinstance(e,HTTPException):
            code = e.code
            msg = e.description
            status_code = 404
            return  APIException(status_code,msg,code)
        else:
            #log
            if  not  app.config["DEBUG"]:
                return APIException()
            else:
                raise e
    else:
        print(e)
        return web_errors()


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8081)

