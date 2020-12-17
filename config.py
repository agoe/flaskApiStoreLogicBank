"""Flask configuration variables."""
from os import environ, path
import utility as util

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    if 'sqlite' in SQLALCHEMY_DATABASE_URI:
        util.log('Basedir: '+basedir)
        SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(basedir, "sqlite.db")

    util.log(SQLALCHEMY_DATABASE_URI)

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = False

