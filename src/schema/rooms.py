from typing_extensions import Required
import mongoengine
from .bookings import Booking
from mongoengine import ReferenceField


class Room(mongoengine.Document):
    room_name = mongoengine.StringField(required=True)
    max_people = mongoengine.IntField(required=True)
    bookings = mongoengine.ListField(ReferenceField(Booking))

    meta = {
        'db_alias': 'core',
        'collecition': 'rooms'
    }
