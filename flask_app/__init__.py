"""Initialize Flask app."""
from flask import Flask
from flask_restful import Api
from resources import api_resources
import utility as util


def create_app():
    app: Flask = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    util.log("create_app")
    util.log(app.config)
    #  db.init_app(app)

#    with app.app_context():
#  from . import routes  # Import routes
#  db.create_all()  # Create database tables for our data models
    return app


def create_test_app():
    app: Flask = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    util.log("create_app")
    util.log(app.config)
    #  db.init_app(app)

#    with app.app_context():
#  from . import routes  # Import routes
#  db.create_all()  # Create database tables for our data models
    api: Api = Api(app)
    api_resources.configure_api(app, api)
#    app.run(host="0.0.0.0", port=5000)
    return app
