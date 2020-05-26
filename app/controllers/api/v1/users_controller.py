"""Users Controller"""

from flask import jsonify
from app.controllers.api import api_v1 as api
from app.models.user import User
from app.util.db import DbUtil as db


@api.route('/users')
def index():
    """Calls api/v1/users

    This controller returns all users
    """
    users = db.get_all(User)
    print(users)
    # return jsonify(users)
    return "works!"
