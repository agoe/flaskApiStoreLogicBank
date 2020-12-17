from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.security import authenticate, identity
from .store import *
from .item import *
from .user import *


def configure_api(app: Flask, api: Api):
    JWT(app, authenticate, identity)  # /auth

    api.add_resource(Store, "/store/<string:name>")
    api.add_resource(StoreList, "/stores")
    api.add_resource(Item, "/item/<string:name>")
    api.add_resource(ItemList, "/items")
    api.add_resource(UserRegister, "/register")
