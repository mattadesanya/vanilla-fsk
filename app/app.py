"""Main Flask Application

The main flask application starts here
"""

from flask import Flask
from app.database import db
from app.api import api as api_blueprint
from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.register_blueprint(api_blueprint)
    db.init_app(app)

    return app
