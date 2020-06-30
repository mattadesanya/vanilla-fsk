from app.util.db_util import DbUtil as db
from app.models.role import Role
from app.models.permission import Permission
from app.models.role_permission import RolePermission
from faker import Faker

fake = Faker()


def seed_role():
    roles = ['admin', 'user']
    for role in roles:
        role = Role(role=role, default=(role == 'user'))
        db.save_to_db(role)


def seed_permission():
    permissions = ['VIEW_USERS', 'CREATE_USER']
    for permission in permissions:
        permission = Permission(permission=permission)
        db.save_to_db(permission)


def map_role_to_permission():
    role = 'admin'
    admin_mappings = [
                        {'role': role, 'permission': 'CREATE_USER'},
                        {'role': role, 'permission': 'VIEW_USERS'}
                    ]

    # I intentionally left this style of creating dictionaries
    # for learning purposes
    role = 'user'
    user_mappings = [
                        dict(role=role, permission='VIEW_USERS')
                    ]

    for admin_mapping in admin_mappings:
        admin_role_permissions = RolePermission(**admin_mapping)
        db.save_to_db(admin_role_permissions)

    for user_mappings in user_mappings:
        user_role_permissions = RolePermission(**user_mappings)
        db.save_to_db(user_role_permissions)
