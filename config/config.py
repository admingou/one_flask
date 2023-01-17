from datetime import timedelta

UPLOAD_FOLDER = "upload"


#mysql数据库密码
SQLALCHEMY_TRACK_MODIFICATIONS = True
mysql_pwd = "LsPasswd@12345"
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://admin:{mysql_pwd}@192.28.1.234:3306/cloud_pan_date?charset=utf8"
SQLALCHEMY_COMMIT_ON_TEARDOWN = True

#redis数据库
redis_host = "192.28.1.238"
redis_port = 6379
redis_db = 10


SECRET_KEY = "gou24354354654654765fbghmujuiulibtrb"
#session过期时间
PERMANENT_SESSION_LIFETIME = timedelta(days=7)


# 邮件服务器IP（域名）
mail_server_ip = "smtp.163.com"
# 邮件服务器端口
mail_server_port = 465

# 发送邮箱账号
send_user = "gslymykey@163.com"

# 发送邮箱密钥(通过自带工具加密后使用以防泄密)
send_pass = "VGs1S1ZFeFBWRk5HVDFCVlYwVkVWdz09RlphbXN5VGtk"

# 邮件接收者
receive_list = ["gousl@fusionskye.com"]

# 邮件附件（可添加多个，附件绝对路径）
file_path_list = []

# 邮件主题
send_title = "高效魔方验证码"

# 邮件内容(可按照格式编写)
message = """
   

"""
