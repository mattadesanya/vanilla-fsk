"""Application Factory"""

from flask import Flask
from app.database import db
from app.controllers.api import api_v1 as api_v1_blueprint
from config import config


def create_app(config_name):
    """
    The create_app() function is the application factory,
    which takes as an argument the name of a
    configuration to use for the application.
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.register_blueprint(api_v1_blueprint)
    db.init_app(app)

    return app
