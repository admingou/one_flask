from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from  sqlalchemy import Column,DateTime



db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    create_time = Column(DateTime, default=datetime.now)

    def set_attrs(self, dicts):
        """
        添加数据
        :param dicts: 数据源
        :return: 添加状态
        """
        print(dicts,type(dicts))
        if dicts:
            for k, v in dicts.items():
                if hasattr(self, k) and k != "id" and k != "create_time" and k != "update_time" and k !="codes":
                    setattr(self, k, v)