from datetime import timedelta

UPLOAD_FOLDER = "upload"
#数据库密码
SQLALCHEMY_TRACK_MODIFICATIONS = True

mysql_pwd = "LsPasswd@12345"
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://admin:{mysql_pwd}@192.28.1.234:3306/cloud_pan_date?charset=utf8"
SQLALCHEMY_COMMIT_ON_TEARDOWN = True


SECRET_KEY = "gou24354354654654765fbghmujuiulibtrb"
#session过期时间
PERMANENT_SESSION_LIFETIME = timedelta(days=7)

