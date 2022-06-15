from  one_all_web.models.base_model import db
from sqlalchemy import Integer,String,Column,DateTime
from datetime import datetime
from one_all_web.models.base_model import Base



class CloudPan(Base):
    #id
    id = Column(Integer, primary_key=True, autoincrement=True)
    #用户id
    user_id = Column(Integer, nullable=False)
    #文件名
    file_name = Column(String(64),unique=True, nullable=False)
    #存储位置
    file_path = Column(String(64),unique=True, nullable=False)
    #文件MD5
    md5s = Column(String(64),unique=True, nullable=False)
    #文件描述
    msg = Column(String(128), nullable=False)
    #下载次数
    down_num = Column(Integer, nullable=False)
    #更新时间
    update_time = Column(DateTime, default=datetime.now)
    __tablename__ = 'cloud_pan'



    def get_date(self, names=None):
        """
        查询数据
        :param names: 查询字段
        :return:
        """
        date = CloudPan.query.filter().all()
        if names:
            date = CloudPan.query.filter_by(names.keys()[0] == names.get(names.keys()[0])).all()
        return date

    def update_date(self, id, updates):
        """
        更新数据
        :param updates: 更新内容字典
        :return: 更新状态
        """
        try:
            updates["update_time"] = datetime.now()
            CloudPan.query.filter(id == id).update(updates)
            db.session.commit()
            return 0
        except:
            return 1

    def delete_date(self, id):
        """
        删除数据
        :param name_type:
        :param id:
        :return:
        """
        try:
            CloudPan.query.filter(id == id).delete()
            db.session.commit()
            return 0
        except:
            return 1