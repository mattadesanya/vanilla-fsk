"""API Blueprint"""

from flask import Blueprint

api_v1 = Blueprint('api', '__name__', url_prefix='/v1')
