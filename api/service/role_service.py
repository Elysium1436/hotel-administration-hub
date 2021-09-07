from typing import List
import logging
from .dataservice_utils import table_print_schema
from ..model.roles import Role, Permission

logger = logging.getLogger(__name__)


def add_role(role_name, permissions: List[Permission], return_instance=False):
    role = Role()
    role.role_name = role_name
    role.permissions = permissions

    role.save()
    if return_instance:
        return role


def view_roles():
    table_print_schema(Role, ['role_name', 'permissions'])


def delete_role(role_name):
    role = Role.objects(role_name=role_name)
    role.delete()


def find_role(role_name: str) -> Role:

    try:
        role = Role.objects(role_name=role_name).first()
        assert isinstance(role, Role)

    except AssertionError:
        logger.error('Assertion Error', exc_info=True)
        return None

    logging.info(f'Role {role.name} has been found.')
    return role


def find_roles_by_permission(permission) -> list:
    roles = Role.objects().all()
    roles_with_permission = []
    for role in roles:
        if permission in role.permissions:
            roles_with_permission.append(role)

    return roles_with_permission
