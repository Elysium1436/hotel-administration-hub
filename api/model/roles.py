from enum import unique
import mongoengine
import enum
from enum import auto


class Permission(enum.Enum):
    USER = "USER"
    ROOM = "ROOM"
    GUEST = "GUEST"
    ROLE = "ROLE"
    BOOKING = "BOOKING"

    @classmethod
    def list_name(cls):
        return list(map(lambda c: c.name, cls))


class Role(mongoengine.Document):
    role_name = mongoengine.StringField(required=True, unique=True)
    permissions = mongoengine.ListField(mongoengine.EnumField(Permission))
