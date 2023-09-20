from sqlalchemy import create_engine


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
        self.engine = None

    def init_app(self):
        self.engine = create_engine(
            f"mysql+pymysql://{self.user}:{self.password}@{self.host}/{self.dbname}?charset=utf8mb4")


if __name__ == '__main__':
    pass
