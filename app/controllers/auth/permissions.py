"""Permission Required Decorator"""

from functools import wraps
from flask_jwt_extended import get_jwt_claims
from app.redis import redis_client
from app.models.role_permission import RolePermission

Permissions = {
    'Create_User': 'CREATE_USER',
    'View_Users': 'VIEW_USERS',
    'View_User': 'VIEW_USER'
}

REDIS_KEY_PREFIX = "fsk:role"


def get_permissions(role):
    """Get permissions for a role from db"""
    permissions = []
    role_permissions = RolePermission.query.filter_by(role=role)
    for role_permission in role_permissions:
        permissions.append(role_permission.permission)

    return permissions


def permission_required(given_permission):
    """permission_required decorator"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            claims = get_jwt_claims()

            # construct redis key for the given role
            redis_key = "{}:{}".format(REDIS_KEY_PREFIX, claims['role'])

            # look in redis for the given list of permissions
            redis_permissions = redis_client.lrange(redis_key, 0, -1)

            permissions = [p.decode("utf-8") for p in redis_permissions]

            if permissions == []:     # means it's not in Redis
                # get the permissions from the database
                permissions = get_permissions(claims['role'])
                # add permissions to Redis
                for permission in permissions:
                    redis_client.lpush(redis_key, permission)

            # if the given permission is not in the list of permissions
            # for the role of this user, block this user
            if given_permission not in permissions:
                return {
                    "msg": "Insufficient Permissions"
                }, 401

            return func(*args, **kwargs)

        return wrapper

    return decorator
