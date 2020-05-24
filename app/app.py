"""Main Flask Application

The main flask application starts here
"""

from flask import Flask
from app.database import db
from app.controllers.api import api_v1 as api_v1_blueprint
from config import config
from app.controllers.api.v1 import *


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.register_blueprint(api_v1_blueprint)
    db.init_app(app)

    return app
