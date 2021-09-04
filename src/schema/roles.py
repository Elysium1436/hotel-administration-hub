from enum import unique
import mongoengine
import enum
from enum import auto


class Permission(enum.Enum):
    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
    USER = 'USER'
    ROOM = 'ROOM'
    GUEST = 'GUEST'
    ROLE = 'ROLE'
    BOOKING = 'BOOKING'


class Role(mongoengine.Document):
    role_name = mongoengine.StringField(required=True, unique=True)
    permissions = mongoengine.ListField(mongoengine.EnumField(Permission))
    meta = {
        'db_alias': 'core',
        'collection': 'roles'
    }
