from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

ModelBase = declarative_base() #<-元类



def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.colums}


def ToDict(cls):
    cls.to_dict = to_dict
    return cls


@ToDict
class User(ModelBase):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    user_name = Column(String(20))
    gender = Column(Boolean())
    email = Column(Integer())
    phone = Column(String(15))
    age = Column(Integer())
    follow = Column(String(20))
    fans = Column(Integer())
    create_date = Column(DateTime())
    update_date = Column(DateTime())
