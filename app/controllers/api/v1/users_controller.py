"""Users Controller"""

from flask import jsonify, request
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, fresh_jwt_required
from app.controllers.api import api_v1 as api
from app.models.user import User
from app.serializers.api.v1.user_serializer import users_serializer, \
                                                    user_serializer
from app.util.db_util import DbUtil as db


@api.route('/users', methods=['POST'])
@fresh_jwt_required
def create_user():
    """ Create a new user """
    json_data = request.get_json()
    if not json_data:
        return jsonify({'msg': 'no valid input'}), 400

    # validate and deserialize the input
    try:
        new_user = user_serializer.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 422

    user = User(username=new_user['username'], password=new_user['password'])
    db.save_to_db(user)
    result = user_serializer.dump(user)
    return jsonify({'msg': 'User Created', 'data': result}), 201


@api.route('/users')
@jwt_required
def get_users():
    """Calls /v1/users

    This controller returns all users
    """
    users = db.get_all(User)
    result = users_serializer.dump(users)
    return jsonify({'data': result})


@api.route('/users/<fancy_id>')
@jwt_required
def get_user(fancy_id):
    """Calls /v1/users/id

    This controller returns a particular used by id
    """
    user = db.get_by_fid(User, fancy_id)
    result = user_serializer.dump(user)
    return jsonify({'data': result})
