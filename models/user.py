from sqlalchemy import Column, Integer, String
from db import Base, Session


class UserModel(Base):
    __tablename__ = 'users'
    query = Session.query_property()

    id = Column(Integer, primary_key=True)
    username = Column(String(length=80))
    password = Column(String(length=80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        Session.add(self)
        Session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
