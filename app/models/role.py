# pylint: disable=no-member
# pylint: disable=too-few-public-methods

"""Role Model (No Pun Intended)"""

from app.models.model import Model
from app.database import db


class Role(Model):
    """Role model class"""

    __tablename__ = 'roles'

    role = db.Column(db.String(20), unique=True, nullable=False)
    default = db.Column(db.Boolean, default=False, index=True)
    users = db.relationship('User', backref='roles', lazy='dynamic')
    role_permissions = db.relationship('RolePermission', backref='roles')

    def __init__(self, role=None, default=False):
        self.role = role
        self.default = default

    def __repr__(self):
        return '<Role {}>'.format(self.role)
