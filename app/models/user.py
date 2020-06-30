# pylint: disable=no-member
# pylint: disable=too-few-public-methods

"""User Model"""

from flask_bcrypt import Bcrypt
from app.models.model import Model
from app.database import db

# pylint: disable=unused-import
import app.models.role  # noqa: F401


class User(Model):
    """User model class"""

    __tablename__ = 'users'

    DEFAULT_ROLE = 'user'

    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    last_login = db.Column(db.DateTime, onupdate=db.func.current_timestamp())
    role = db.Column(db.String(20), db.ForeignKey('roles.role'))

    def __init__(self, username=None, password=None, role=DEFAULT_ROLE):
        self.username = username
        self.password = Bcrypt().generate_password_hash(password)\
                                .decode('utf-8')
        self.role = role

    def check_password(self, password):
        """ This method is called whenever a user tries to login """
        return Bcrypt().check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
