"""Auth Controller"""

import logging
from datetime import datetime
from flask import request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token,\
                                get_jwt_identity, jwt_refresh_token_required,\
                                get_raw_jwt
from app.database import db
from app.models.user import User
from app.models.blacklist_token import BlacklistToken
from app.controllers.auth import auth_blueprint as auth, jwt

logger = logging.getLogger(__name__)


class TokenException(Exception):
    """ TokenException class to handle exceptions """
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


# pylint: disable=no-member
def blacklist_token(token):
    """ puts a token in the BlacklistToken table """
    blacklist = BlacklistToken(token=token)
    try:
        db.session.add(blacklist)
        db.session.commit()
        return True
    except TokenException as err:
        logging.error(err)
        return False


def update_last_login(username):
    """ update the user table last login field """
    user = User.query.filter_by(username=username).first()
    user.last_login = datetime.now()
    db.session.commit()
# pylint: disable=no-member


@jwt.token_in_blacklist_loader
def is_token_blacklisted(refresh_token):
    """this method checks if a refresh token
    is in the Blacklisted tokens table
    """
    jti = refresh_token['jti']
    return BlacklistToken.check_blacklist(jti)


@auth.route('/login', methods=['POST'])
def login_user():
    """ Login user """
    payload = request.json
    resp = {}
    try:
        username = payload.get('username')
        password = payload.get('password')

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            access_token = create_access_token(identity=user.f_id,
                                               fresh=True)
            refresh_token = create_refresh_token(user.f_id)

            if access_token:
                update_last_login(username)
                ret = {
                    'msg': 'Login Successful',
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }
                resp = jsonify(ret), 200
        else:
            resp = jsonify({'msg': 'Username or password mismatch'}), 401

    except TokenException as err:
        logger.error(err)
        resp = jsonify({'msg': 'Unknown error occurred. Try again'}), 500

    return resp


@auth.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    """Refresh endpoint
    To help generate a non-fresh access token whenever
    the client attempts to call an endpoint with an expired
    access token
    """
    current_user = get_jwt_identity()
    resp = {
        'access_token': create_access_token(identity=current_user)
    }
    return jsonify(resp), 200


@auth.route('/logout', methods=['DELETE'])
@jwt_refresh_token_required
def logout():
    """ the logout method
    accepts request as input,
    it makes a call to JwtToken's decode_token method
    and then blacklists the token gotten.
    """
    refresh_token = get_raw_jwt()
    blacklisted = blacklist_token(refresh_token['jti'])
    if blacklisted:
        return jsonify({'msg': 'Logout Successful'}), 200

    return jsonify({'msg': 'Logout failed'}), 500
