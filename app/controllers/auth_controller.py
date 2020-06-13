"""API Blueprint"""

from flask import Blueprint, request
from app.lib.authorization.auth_lib import Auth

auth = Blueprint('auth', '__name__', url_prefix='/auth')


@auth.route('/login', methods=['POST'])
def login_user():
    """ Login user """
    login_credentials = request.json
    return Auth.login(login_credentials)


@auth.route('/logout', methods=['GET'])
def logout():
    """ Logout user """
    return Auth.logout(request)
