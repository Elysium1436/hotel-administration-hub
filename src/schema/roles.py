from enum import unique
import mongoengine
import enum
from enum import auto


class Permission(enum.Enum):
    USER = auto()
    ROOM = auto()
    GUEST = auto()
    ROLE = auto()
    BOOKING = auto()


class Role(mongoengine.EmbeddedDocument):
    role_name = mongoengine.StringField(required=True, unique=True)
    permissions = mongoengine.ListField(mongoengine.EnumField(Permission))
