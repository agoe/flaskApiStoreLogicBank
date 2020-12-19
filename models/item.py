from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from db import Base, Session


class ItemModel(Base):
    __tablename__ = 'items'
    query = Session.query_property()
    id = Column(Integer, primary_key=True)
    name = Column(String(length=80))
    price = Column(Float(precision=2))

    store_id = Column(Integer,  ForeignKey('stores.id'), nullable=False,)
    #  store = relationship('StoreModel')
    store = relationship("StoreModel", back_populates="items")

    def __init__(self, name = None, price = None, store_id = None):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'id': self.id, 'name': self.name, 'price': self.price}

    @classmethod
    def find_by_id(cls, _id: int):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, name: str):
        return cls.query.filter(ItemModel.name == name).first()

    def save_to_db(self):
        Session.add(self)
        Session.commit()

    def delete_from_db(self):
        Session.delete(self)
        Session.commit()
