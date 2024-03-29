"""Application Factory"""

from flask import Flask
from flask_migrate import Migrate
from app.database import db
from app.redis import redis_client
from app.controllers.api import api_v1 as api_v1_blueprint
from app.controllers.auth import auth_blueprint, jwt
from config import config


def create_app(config_name):
    """
    The create_app() function is the application factory,
    which takes as an argument the name of a
    configuration to use for the application.
    """
    app = Flask(__name__)
    migrate = Migrate()

    app.config.from_object(config[config_name])

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(api_v1_blueprint)

    db.init_app(app)
    jwt.init_app(app)
    redis_client.init_app(app)
    migrate.init_app(app, db)

    return app
