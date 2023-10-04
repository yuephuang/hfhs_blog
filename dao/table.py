from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base


def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


def ToDict(cls):
    cls.to_dict = to_dict
    return cls

#
# @ToDict


Base = declarative_base()


@ToDict
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    password = Column(String)
    user_name = Column(String(20))
    gender = Column(Boolean())
    email = Column(Integer())
    phone = Column(String(15))
    age = Column(Integer())
    follow = Column(String(20))
    fans = Column(Integer())
    create_date = Column(DateTime())
    update_date = Column(DateTime())


@ToDict
class ImageGroupsType(Base):
    __tablename__ = 'image_groups_type'

    id = Column(Integer, primary_key=True)
    image_group_name = Column(String)
    create_by = Column(Integer())
    create_date = Column(DateTime())
    update_date = Column(DateTime())


@ToDict
class ImageUser(Base):
    __tablename__ = 'image_user'

    id = Column(Integer, primary_key=True)
    image_name = Column(String)
    image_type = Column(String)
    image_md5 = Column(String)
    create_by = Column(Integer())
    create_date = Column(DateTime())
    update_date = Column(DateTime())


@ToDict
class ImageMd5Url(Base):
    __tablename__ = 'image_md5_url'

    image_md5 = Column(String, primary_key=True)
    image_url = Column(String)
    count = Column(Integer())
