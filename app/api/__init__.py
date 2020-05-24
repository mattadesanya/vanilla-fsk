from flask import Blueprint
from app.api.controllers.v1 import users

api = Blueprint('api', '__name__')
