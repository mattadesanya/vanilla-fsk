# pylint: disable=no-member
# pylint: disable=too-few-public-methods

"""RolePermission Model"""

from app.models.model import Model
from app.database import db

# pylint: disable=unused-import
import app.models.role  # noqa: F401
import app.models.permission  # noqa: F401


class RolePermission(Model):
    """RolePermission model class"""

    __tablename__ = 'role_permissions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(
        db.String(20),
        db.ForeignKey('roles.role'),
        nullable=False)
    permission = db.Column(
        db.String(30),
        db.ForeignKey('permissions.permission'),
        nullable=False)
