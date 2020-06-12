"""Users Controller"""

from flask import jsonify
from app.controllers.api import api_v1 as api
from app.models.user import User
from app.serializers.api.v1.user_serializer import users_serializer, \
                                                    user_serializer
from app.util.db_util import DbUtil as db
from app.lib.authorization.auth_decorator import token_required


@api.route('/users')
@token_required
def get_users():
    """Calls api/v1/users

    This controller returns all users
    """
    users = db.get_all(User)
    result = users_serializer.dump(users)
    return jsonify({'data': result})


@api.route('/users/<f_id>')
@token_required
def get_user(f_id):
    """Calls api/v1/users/id

    This controller returns a particular used by id
    """
    user = db.get_by_fid(User, f_id)
    result = user_serializer.dump(user)
    return jsonify({'data': result})


# @api.route('/users/<f_id>', methods=['PUT'])
# def update_user():
#     json_data = request.get_json()
#     if not json_data:
#         return jsonify({'message': 'no valid input'}), 400
