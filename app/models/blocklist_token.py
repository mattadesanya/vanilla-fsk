# pylint: disable=no-member
# pylint: disable=too-few-public-methods

"""Blocklist Model"""

from datetime import datetime
from app.database import db


class BlocklistToken(db.Model):
    """
    Token Model for storing JWT tokens
    """
    __tablename__ = 'blocklist_tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    blocklisted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = token
        self.blocklisted_on = datetime.now()

    @staticmethod
    def check_blocklist(auth_token):
        """ check whether auth token has been blacklisted """
        result = BlocklistToken.query.filter_by(token=str(auth_token)).first()

        return result

    def __repr__(self):
        return '<id: token: {}'.format(self.token)
