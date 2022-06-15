from one_all_web.models.base_model import db
from datetime  import datetime
from  sqlalchemy import Column,String,Integer,DateTime
from one_all_web.models.base_model import Base


class AccObject(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    #用户名
    username = Column(String(64),unique=True, nullable=False)
    #角色
    types = Column(String(32),unique=True, nullable=False)
    #访问权限
    acc_object = Column(String(64),unique=True, nullable=False)
    #头像
    num = Column(String(64),unique=True, nullable=False)
    #账号状态
    status = Column(String(32), nullable=False)
    #邮箱
    email = Column(String(64),unique=True, nullable=False)
    #过期时间
    end_time = Column(DateTime,unique=True, nullable=False)
    #更新时间
    update_time = Column(DateTime, default=datetime.now)
    __tablename__ = 'acc_object'


    def __repr__(self):
        return '<Role:%s>' % (self.id)

    def create_date(name_type, dicts):
        """
        添加数据
        :param name_type: 模型类
        :param dicts: 添加数据字典
        :return: 创建状态
        """
        try:
            da = name_type()
            da.set_dates(dicts)
            db.session.add(da)
            db.session.commit()
            return 0
        except Exception as f:
            print(f)
            return 1

    def get_date(name_type, names=None):
        """
        查询数据
        :param names: 查询字段
        :return:
        """
        date = name_type.query.filter().all()
        if names:
            date = name_type.query.filter_by(names.keys()[0] == names.get(names.keys()[0])).all()
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