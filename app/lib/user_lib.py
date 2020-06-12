"""User Library

The User Lib provides all the methods used by
users on the app
"""
from app.models.user import User
from app.util.db_util import DbUtil as db


class UserLib:
    """ UserLib Class """
    @classmethod
    def create_user(cls, new_user):
        """ this method creates a new user object """
        username = new_user['username']
        password = new_user['password']
        user = User(username=username, password=password)
        db.save_to_db(user)
        return user
