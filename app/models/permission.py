# pylint: disable=no-member
# pylint: disable=too-few-public-methods

"""Permission Model"""

from app.models.model import Model
from app.database import db


class Permission(Model):
    """Permission model class"""

    __tablename__ = 'permissions'

    permission = db.Column(db.String(30), unique=True, nullable=False)
    role_permissions = db.relationship('RolePermission', backref='permissions')

    def __init__(self, permission=None):
        self.permission = permission

    def __repr__(self):
        return '<Permission {}>'.format(self.permission)
