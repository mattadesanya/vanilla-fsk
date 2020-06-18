"""Auth Blueprint"""

from flask import Blueprint
from flask_jwt_extended import JWTManager

auth_blueprint = Blueprint('auth', '__name__', url_prefix='/auth')
jwt = JWTManager()
