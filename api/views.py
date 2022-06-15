from one_all_web.models.User import User
from one_all_web.models.base_model import db
from one_all_web.error.codes import Success,Error
from flask import request,session
from  . import  api




@api.route("/register", methods=["POST"])
def  user_register():
    """
    用户注册接口
    :return:
    """
    if request.method == "POST":
      try:
        user = User()
        print(request.json)
        if not user.get_date(names=request.json):
            user.set_attrs(request.json)
            db.session.add(user)
            db.session.commit()
            return Success(msg="注册成功")
        return Success(msg="该用户名或邮箱已注册,请勿重复提交")
      except Exception as f:
          print(f)
          return Success(msg=str(f))



@api.route("/delete_session", methods=["GET"])
def  delete_session():
    if request.method == "GET":
        if session.get("usernameID"):
            session.pop("usernameID")
            return Success(msg="注销成功")
        return Error(msg="用户未登录")