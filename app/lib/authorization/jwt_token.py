"""JWT Token"""

import os
import logging
from datetime import datetime, timedelta
import jwt
from config import config
from app.models.blacklist_token import BlacklistToken


PY_ENV = os.environ.get('PY_ENV') or 'default'

key = config[PY_ENV].SECRET_KEY

logger = logging.getLogger(__name__)


class TokenException(Exception):
    """ TokenException class to handle exceptions """
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class JwtToken:
    """ The JwtToken class

    Handles everything related to Jwt
    """
    @classmethod
    def generate_token(cls, user_id):
        """
        Generate Auth Access Token
        """
        print(key)
        try:
            # create a payload with an expiration time
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=10),
                'iat': datetime.utcnow(),
                'sub': user_id
            }

            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )

        except TokenException as err:
            logging.error(err)

    @classmethod
    def decode_token(cls, auth_token):
        """
        Decode Auth Access Token
        :param Auth Token
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                raise TokenException("The Token has been blacklisted")

            return payload.get('sub')
        except jwt.ExpiredSignatureError:
            # the token is expired, return an error
            raise TokenException("Expired Token.\
            Login to generate a new token")
        except jwt.InvalidTokenError as err:
            # return error when the token is invalid
            logging.error(err)
            raise TokenException("Invalid Token. Register User or Login")
