from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy import or_
from one_all_web.models.base_model import db
from  sqlalchemy import Column,String,DateTime,Integer
from one_all_web.models.base_model import Base
import datetime


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    #用户名
    username = Column(String(64),unique=True, nullable=False)
    #角色
    types = Column(String(32), nullable=False,default="an")
    #头像
    phone = Column(String(64), nullable=False, default="")
    #账号状态
    status = Column(Integer, nullable=False, default=1)
    #邮箱
    email = Column(String(64),unique=True, nullable=False)
    #过期时间
    end_time = Column(DateTime,nullable=False, default=datetime.datetime.now()+datetime.timedelta(days=365))
    #更新时间
    update_time = Column(DateTime, default=datetime.datetime.now)
    #密码
    _password = Column("password",String(128), comment='密码')
    __tablename__ = 'g_user'

    @property
    def  password(self):
        return self._password

    @password.setter
    def  password(self, x_password):
        """
        明文加密
        :param x_password:  明文密码
        :return:
        """
        self._password = generate_password_hash(x_password)


    def  check_password(self,x_password):
        """

        :param x_password:  明文密码
        :return:
        """
        #print("密码:%s      密文:%s"%(x_password, self._password))
        #print(check_password_hash(self._password, x_password))
        return  check_password_hash(self._password, x_password)

    def __repr__(self):
        return str(self.id)



    def get_date(self, names=None):
        """
        查询数据
        :param names: 查询字段
        :return:
        """
        date = User.query.filter().all()
        if names:
            date = User.query.filter(or_( User.username == names.get("username"),User.email == names.get("email"))).all()
        return date

    def update_date(name_type, id, updates):
        """
        更新数据
        :param updates: 更新内容字典
        :return: 更新状态
        """
        try:
            updates["update_time"] = datetime.datetime.now()
            name_type.query.filter(id == id).update(updates)
            db.session.commit()
            return 0
        except:
            return 1

    def delete_date(name_type, id):
        """
        删除数据
        :param name_type:
        :param id:
        :return:
        """
        try:
            name_type.query.filter(id == id).delete()
            db.session.commit()
            return 0
        except:
            return 1


