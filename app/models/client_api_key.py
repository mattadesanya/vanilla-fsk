# pylint: disable=no-member
# pylint: disable=too-few-public-methods

"""ClientApiKey Model"""

from passlib.apps import custom_app_context as pwd_context
from app.models.model import Model
from app.database import db


class ClientApiKey(Model):
    """
    Model for storing Client Api Keys
    """
    __tablename__ = 'client_api_keys'

    name = db.Column(db.String(100), unique=True, nullable=False)
    key_hash = db.Column(db.String(200), unique=True, nullable=False)

    def __init__(self, name, key_hash):
        self.name = name
        self.key_hash = key_hash

    def hash_key(self, key):
        """ hash the key generated """
        self.key_hash = pwd_context.encrypt(key)

    def verify_key(self, key):
        """Verify the incoming key"""
        return pwd_context.verify(key, self.key_hash)

    def __repr__(self):
        return '<id: name: {}'.format(self.name)
