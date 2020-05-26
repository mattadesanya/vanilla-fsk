"""Users Controller"""

from flask import jsonify
from app.controllers.api import api_v1 as api
from app.daos.user_dao import UserDAO as user_dao


@api.route('/users')
def index():
    """Calls api/v1/users

    This controller returns all users
    """
    users = user_dao.get_all()
    print(users)
    # return jsonify(users)
    return "works!"
