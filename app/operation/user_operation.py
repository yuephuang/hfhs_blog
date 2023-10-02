from datetime import datetime

from domain.MysqlClient import mysql_client
from log.logger_main import logger
from dao.table import User


class UserOperation:
    def __init__(self):
        self.logger = logger.main()
        self.client = mysql_client
        self.gender = {
            "man": 0,
            "woman": 1
        }

    def get_user_info(self, _id):
        results = self.client.query_one([User], [User.id == _id])
        # if not results:
        #     raise
        res = results.to_dict()
        return res

    def register_user(self, parser: dict):
        insert_data = User(
            user_name=parser.get("user_name"),
            password=parser.get("password"),
            gender=self.gender.get(parser.get("gender"), 2),
            email=parser.get("email"),
            phone=parser.get("phone"),
            age=parser.get("age"),
            follow=parser.get("follow"),
            fans=parser.get("fans", 0),
            create_date=datetime.now(),
            update_date=datetime.now(),
        )
        try:
            self.client.insert([insert_data])
            return True
        except Exception as e:
            self.logger.error(f"insert Error, parser: {parser}, e: {e}")
            return False
