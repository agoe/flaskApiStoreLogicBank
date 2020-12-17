"""App entry point."""
import db
import utility as util
from flask import Flask
from flask_restful import Api
from flask_app import create_app
from resources import api_resources

app: Flask = create_app()

# with app.app_context():
#  from . import routes  # Import routes
api: Api = Api(app)
api_resources.configure_api(app, api)

util.log("__name__: " + __name__)
if __name__ == "__main__":  # "wsgiapp":
    import models
    db.create_tables()
    import logic
    app.run(host="0.0.0.0", port=5000)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.Session.remove()


"""
Enable CORS. Disable it if you don't need CORS
https://parzibyte.me/blog
"""


@app.after_request
def after_request(response):
    response.headers[
        "Access-Control-Allow-Origin"] = "*"  # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = \
        "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response
