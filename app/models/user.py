"""User Model"""

from app.models.model import Model
from app.database import db


class User(Model):
    """User model class"""

    __tablename__ = 'user'

    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    last_login = db.Column(db.DateTime, onupdate=db.func.current_timestamp())

    def __init__(self, id=None, username=None, password=None):
        self.id = id
        self.username = username
        self.password = password
