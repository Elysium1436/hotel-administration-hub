from schema.bookings import Booking
from schema.guests import Guest
from schema.users import User
from schema.rooms import Room
from schema.roles import Role, Permission
import data_service_utils
import logging
import enum
from typing import List

logger = logging.getLogger(__name__)


def add_user(name: str, password: str, email: str, role_name: str = None):
    user = User()
    user.username = name
    user.password = password
    user.email = email

    if role_name is not None:
        user.role.append(data_service_utils.find_role(role_name))
    user.save()


def add_role(role_name: str, permissions: List[enum.Enum] = None):
    role = Role()
    role.role_name = role_name
    role.permissions = permissions
    role.save()


def print_user_info(username: str):

    user = User.objects(username=username)
    logger.debug(
        f'{user.username} {user.email} {user.password_hash} {user.roles.name}')
    print(f'{user.username} {user.email} {user.password_hash} {user.roles.name}')
