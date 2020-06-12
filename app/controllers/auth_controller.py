"""API Blueprint"""

from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from app.lib.user_lib import UserLib as user_lib
from app.lib.authorization.auth_lib import Auth
from app.serializers.api.v1.user_serializer import user_serializer

auth = Blueprint('auth', '__name__', url_prefix='/auth')


@auth.route('/register', methods=['POST'])
def create_user():
    """ Create a new user """
    json_data = request.get_json()
    if not json_data:
        return jsonify({'message': 'no valid input'}), 400

    # validate and deserialize the input
    try:
        new_user = user_serializer.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 422

    user = user_lib.create_user(new_user)
    result = user_serializer.dump(user)
    return jsonify({'message': 'User Created', 'data': result}), 201


@auth.route('/login', methods=['POST'])
def login_user():
    """ Login user """
    login_credentials = request.json
    return Auth.login(login_credentials)


@auth.route('/logout', methods=['GET'])
def logout():
    """ Logout user """
    return Auth.logout(request)
