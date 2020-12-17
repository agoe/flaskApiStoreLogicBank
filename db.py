import utility as util

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


#  SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(basedir, "sqlite.db")
#  engine = create_engine(os.environ['SQLALCHEMY_URL'])
from config import Config

SQLALCHEMY_DATABASE_URI = Config.SQLALCHEMY_DATABASE_URI
util.log("Create Engine Uri: "+SQLALCHEMY_DATABASE_URI)
engine = create_engine(SQLALCHEMY_DATABASE_URI)

Session: scoped_session = scoped_session(sessionmaker(bind=engine))
Base: declarative_base = declarative_base()
metadata: MetaData = Base.metadata


def create_tables():
    Base.metadata.create_all(engine)


