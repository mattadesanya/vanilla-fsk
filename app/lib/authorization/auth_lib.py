"""Authentication Library

The Auth Lib provides all the methods used for
authentication on the app
"""
import logging
from datetime import datetime
from app.database import db
from app.models.user import User
from app.models.blacklist_token import BlacklistToken
from app.lib.authorization.jwt_token import JwtToken, TokenException

logger = logging.getLogger(__name__)


def get_auth_token(request):
    """ this method returns the authentication token in the
    request header """
    auth_header = request.headers.get('Authorization')
    auth_token = ''

    if auth_header:
        try:
            auth_token = auth_header.split(" ")[1]
        except IndexError:
            return {
                'status': 'fail',
                'message': 'Bearer token malformed.'
            }, 401

    return auth_token


# pylint: disable=no-member
def blacklist_token(token):
    """ puts a token in the BlacklistToken table """
    blacklist = BlacklistToken(token=token)
    try:
        db.session.add(blacklist)
        db.session.commit()
        return {
            'status': 'success',
            'message': 'Log out Successful'
        }, 200
    except TokenException as err:
        return {
            'status': 'fail',
            'message': str(err)
        }, 200


def update_last_login(username):
    """ update the user table last login field """
    user = User.query.filter_by(username=username).first()
    user.last_login = datetime.now()
    db.session.commit()
# pylint: disable=no-member


class Auth:
    """ The Auth Class """
    @classmethod
    def login(cls, payload):
        """ the login method

        accepts payload containing username and password """
        try:
            username = payload.get('username')
            password = payload.get('password')

            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                auth_token = JwtToken.generate_token(user.f_id)

                if auth_token:
                    update_last_login(username)
                    return {
                        'status': 'success',
                        'message': 'Login Successful',
                        'Authorization': auth_token.decode()
                    }, 200
            else:
                return {
                    'status': 'fail',
                    'message': 'Username or password mismatch'
                }, 401

        except TokenException as err:
            logger.error(err)
            return {
                'status': 'fail',
                'message': 'Unknown error occurred. Try again'
            }, 500

    @classmethod
    def get_logged_in_user(cls, request):
        """ this method returns the payload of the currently logged in user
        whenever it is called """
        auth_token = get_auth_token(request)

        if auth_token:
            try:
                resp = JwtToken.decode_token(auth_token)

                user = User.query.filter_by(f_id=resp).first()

                return {
                    'status': 'success',
                    'data': {
                        'f_id': user.f_id,
                        'username': user.username,
                        'last_login': "{}".format(user.last_login)
                    }
                }, 200

            except TokenException as err:
                return {
                    'status': 'fail',
                    'message': str(err)
                }, 401

        return {
            'status': 'fail',
            'message': 'Provide a valid auth token'
        }, 401

    @classmethod
    def logout(cls, request):
        """ the logout method

        accepts request as input,
        it makes a call to JwtToken's decode_token method
        and then blacklists the token gotten.
        """
        auth_token = get_auth_token(request)

        if auth_token:
            try:
                JwtToken.decode_token(auth_token)

                return blacklist_token(auth_token)

            except TokenException as err:
                return {
                    'status': 'fail',
                    'message': str(err)
                }, 401

        return {
            'status': 'fail',
            'message': 'Provide a valid auth token'
        }, 401
