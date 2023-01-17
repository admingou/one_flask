from one_all_web.models.User import User
from one_all_web.models.YunPan import CloudPan
from one_all_web.models.base_model import db
from one_all_web.error.codes import Success,Error
from one_all_web.libs.check_from import check_from
from flask import render_template,request,send_from_directory,current_app,session,redirect
from . import home
import os
import base64
import time



def login_identify(func):
    """
    装饰器验证是否登录
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        if str(session.get('usernameID')) != 'None':
            return func()
        else:
            return redirect('/login')
    return wrapper




@home.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(current_app.root_path, 'static'),#对于当前文件所在路径,比如这里是static下的favicon.ico
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@home.route("/register",methods=["GET","POST"])
def  user_register():
    """
    用户注册
    :return:
    """
    if request.method == "POST":
        try:
            user = User()
            if not user.get_date(names=check_from(request.json)):
                user.set_attrs(request.json)
                db.session.add(user)
                db.session.commit()
                tu = User.query.filter_by(username=request.json.get("username")).first()
                session["usernameID"] = tu.id
                session["username"] = tu.username
                return Success(msg="注册成功")
            return Error(msg="该用户名或邮箱已注册,请勿重复提交")
        except Exception as f:
            return Success(msg=str(f))
    return  render_template("register.html")


@home.route("/login",methods=["GET","POST"])
def  user_login():
   """
   用户登录
   :return:
   """
   if request.method == "POST":

       data = request.json
       show_user = User()
       user = show_user.get_date(data)
       if user and User.query.filter_by(username=data.get("username")).first().check_password(base64.b64decode(data.get("password")).decode()):
            session["usernameID"] = user[0].id
            session["username"] = user[0].username
            if data.get("code") == "1":
                session.permanent = True
            return Success(msg="登录成功")
       return Error(msg="用户未注册或密码不正确")
   if session.get("usernameID"):
      return redirect("/")
   return  render_template("login.html")



@home.route("/",methods=["GET"])
@login_identify
def  index():
    return render_template("index.html", data={"username":session.get("username","None")})


