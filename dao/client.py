import time
from typing import List

from sqlalchemy import create_engine, QueuePool
from sqlalchemy.orm import Session, sessionmaker

from config.envion import env_config
from log.logger_main import logger


class DbClient:
    def __init__(self, host, port, user, password, **kwargs):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        for key, value in kwargs.items():
            setattr(self, key, value)

    # 初始化
    def init_app(self):
        pass


class MysqlClient(DbClient):
    def __init__(self, host, port, user, password, dbname):
        super().__init__(host, port, user, password, dbname=dbname)
        self.url = f"mysql+pymysql://{self.user}:{self.password}@{self.host}/{self.dbname}?charset=utf8mb4"
        self.engine = self.create_engine()
        self.Session = sessionmaker()
        self.session = Session(bind=self.engine)

    def create_engine(self):
        engine = self.engine = create_engine(
            url=self.url,
            poolclass=QueuePool,
            pool_size=5,
            pool_timeout=30,
            pool_recycle=3600)

        return engine

    def query(self, colum: List, cond=None):
        cond = cond if cond is not None else []
        with self.session as session:
            q = session.query(*colum)
            q.filter(*cond)
        return q

    def query_one(self, colum: List, cond=None):
        q = self.query(colum, cond=cond)
        res = q.first()
        return res

    def query_count(self, colum: List, cond=None) -> int:
        q = self.query(colum, cond=cond)
        res = q.count()
        return res

    def query_order_by(self, colum: List, order_by: List, limit, offset, cond=None):
        q = self.query(colum, cond=cond)
        q = q.order_by(*order_by).limit(limit).offset(offset)
        res = q.all()
        return res


if __name__ == '__main__':
    from dao.table import User

    mysql_client = MysqlClient(host=env_config.get("mysql_host"), port=env_config.get("mysql_prot"),
                               user=env_config.get("mysql_user"), password=env_config.get("mysql_password"),
                               dbname="huang")
    result = mysql_client.query_count([User])
    print(result)
    result = mysql_client.query_order_by([User], order_by=[User.id], limit=10, offset=0)
    print(result)
    result = mysql_client.query_count([User])
    print(result)
