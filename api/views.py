from flask import request,session
from one_all_web.models.User import User
from one_all_web.models.YunPan import CloudPan
from one_all_web.models.base_model import db
from one_all_web.error.codes import Success,Error
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from one_all_web.config.config import SECRET_KEY
from one_all_web.config import redis_store
from one_all_web.libs.send_msg import send_msg
from one_all_web.libs.check_from import check_from
from one_all_web.libs.decode_base64 import decode_base
from one_all_web.libs.ali_dingding import send_code
from  . import  api
import  random
import base64



import os

from one_all_web.libs.get_uuid   import create_id
from werkzeug.utils import secure_filename


@api.route("/code",methods=["POST"])
def  get_codes():
    """
    获取邮箱验证码
    :return:
    """
    if request.method == "POST":
        print(request.json)
        data = check_from(request.json)["email"]
        if data:
            try:
                code = ""
                for _ in range(0,6):
                   code += str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
                if not redis_store.get(data):
                    send_msg("【高效魔方】感谢使用高效魔方,您的验证码为: %s ,五分钟内有效，请勿告知他人！" % (code), data)
                    send_code("【高效魔方】感谢使用高效魔方,您的验证码为: %s ,五分钟内有效，请勿告知他人！" % code)
                    redis_store.set(data, code, 300)
                    redis_store.close()
                    return Success(msg="验证码获取成功")
                return Error(msg="请勿频繁发送验证码")
            except Exception as f:
                print(f)
                return Error(msg="异常错误")
        return Error(msg="未填写邮箱")


@api.route("/registerss", methods=["POST"])
def  user_register():
    """
    用户注册接口
    :return:
    """
    if request.method == "POST":
      try:
        user = User()
        if not user.get_date(names=request.json):
            code = redis_store.get(request.json.get("email"))
            if code and str(code) == request.json.get("codes"):
                user.set_attrs(decode_base(request.json))
                db.session.add(user)
                db.session.commit()
                da = User.query.filter_by(username=request.json.get("username")).first()
                t = Serializer(SECRET_KEY, expires_in=2592000)
                return Success(msg={"token": t.dumps(da.id).decode("utf-8"),"user":da.username})
            return Error(msg="验证码错误")
        return Error(msg="该用户名或邮箱已注册,请勿重复提交")
      except Exception as f:
          print(f)
          return Error(msg=str(f))



@api.route("/login",methods=["POST"])
def  login_get_token():
    if request.method == "POST":
      try:
        da = request.json
        user = User()
        data = user.get_date(names=da)
        if data:
            che_pass = User.query.filter_by(username=da.get("username")).first().check_password(
                decode_base(da).get("password"))
            if che_pass:
                t = Serializer(SECRET_KEY, expires_in=2592000)
                return Success(msg={"token":t.dumps(data[0].id).decode(),"user":data[0].username, "user_id":data[0].id})
            return Error(msg="密码验证错误")
        return Error(msg="用户未注册")
      except Exception as f:
          return Error(msg=str(f))


@api.route("/delete_session", methods=["GET"])
def  delete_session():
    if request.method == "GET":
        if session.get("usernameID"):
            session.pop("usernameID")
            return Success(msg="注销成功")
        return Error(msg="用户未登录")



@api.route("/upload", methods=["POST"])
def  update_cloud():
    da = request.json
    id = da["chunkNumber"]
    name_size = da["fileSize"]
    upload_path = "/opt/"
    #数据存储
    try:
       da["file"].save(secure_filename(upload_path + str(name_size) + str(id)))
       return Success("数据上传成功")
    except Exception as f:
        return Error(str(f))


@api.route("/update_com", methods=["POST"])
def  update_coms():
    da = request.json
    #if os.path.isfile()
    #获取文件名
    file_name = da["fileName"]
    #获取标识符
    name_size = da["fileSize"]
    num = 0
    with  open("/opt/" + file_name, "wb") as fp:
        while True:
            try:
                get_file = "/opt/" + name_size + str(num)
                tt = open(get_file, "rb")
                fp.write(tt.read())
                tt.close()
            except IOError:
                break
            num += 1
            os.remove(get_file)
    return Success(msg="文件保存成功！")



@api.route("/add_date", methods=["POST"])
def  add_file_date():
    try:
        da = request.json
        file_da = CloudPan()
        file_da.set_attrs(da)
        db.session.add(file_da)
        db.session.commit()
        return Success(msg="数据提交成功")
    except Exception as f:
        return Error(msg=str(f))


@api.route("/delete_file", methods=["POST"])
def delete_file_date():
    try:
        da = request.json
        CloudPan().delete_date(da["id"])
        return Success(msg="删除成功")
    except Exception as f:
        return Error(msg="删除失败")

