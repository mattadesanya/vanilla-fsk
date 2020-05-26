"""UserDAO"""

from app.models.user import User
from app.util.db import DbUtil as db


class UserDAO:

    @classmethod
    def get_all(cls):
        return db.get_all(User)
