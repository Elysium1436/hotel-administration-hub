from schema.roles import Role, Permission
import logging
logger = logging.getLogger(__name__)


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
