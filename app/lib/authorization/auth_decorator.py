""" token_required Auth Decorator """
from functools import wraps
from flask import request

from app.lib.authorization.auth_lib import Auth


def token_required(func):
    """ the token_required decorator """
    @wraps(func)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        user_info = data.get('data')

        if not user_info:
            return data, status

        return func(*args, **kwargs)

    return decorated
