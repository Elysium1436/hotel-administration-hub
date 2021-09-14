from typing import List, Union
import logging
from .dataservice_utils import table_print_schema
from ..model.roles import Role, Permission

logger = logging.getLogger(__name__)


def add_role(
    role_name: str, permissions: List[Union[Permission, str]], return_instance=False
):
    print(permissions)
    role = Role()
    role.role_name = role_name
    role.permissions = [Permission[permission] for permission in permissions]

    role.save()
    if return_instance:
        return role


def view_roles():
    table_print_schema(Role, ["role_name", "permissions"])


def delete_role(role_name):
    role = Role.objects(role_name=role_name)
    role.delete()


def find_role(role_name: str) -> Role:

    try:
        role = Role.objects(role_name=role_name).first()
        assert isinstance(role, Role)

    except AssertionError:
        logger.error("Assertion Error", exc_info=True)
        return None

    logging.info(f"Role {role.name} has been found.")
    return role


def get_all_roles():
    return Role.objects().all()


def wipe_roles():
    Role.objects().delete()


def find_roles_by_permission(permission) -> list:
    roles = Role.objects().all()
    roles_with_permission = []
    for role in roles:
        if permission in role.permissions:
            roles_with_permission.append(role)

    return roles_with_permission
