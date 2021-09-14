from enum import Enum
import mongoengine
from werkzeug.security import generate_password_hash, check_password_hash
from .roles import Role
import logging
import datetime


logger = logging.getLogger(__name__)


class User(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    username = mongoengine.StringField(required=True, unique=True)
    email = mongoengine.EmailField(required=True, unique=True)
    password_hash = mongoengine.StringField(required=True)
    role = mongoengine.ReferenceField(Role)

    @property
    def password(self):
        raise AttributeError("Cannot access password")

    @password.setter
    def password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def check_permission(self, permission: Enum):
        for role in self.roles:
            if permission in role.permissions:
                logging.debug(
                    f"User {self.user} permitted with permission {permission}"
                )
                return True
        logging.debug(f"User {self.user} doesn't has the permission {permission}")
        return False

    def set_role_by_name(self, role_name: str):
        role = Role.objects(role_name=role_name).first()
        if role is None:
            raise ValueError("No Role with that name.")
        self.role = role
