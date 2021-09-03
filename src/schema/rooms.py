from typing_extensions import Required
import mongoengine
from schema.bookings import Booking


class Room(mongoengine.Document):
    room_name = mongoengine.StringField(required=True)
    max_people = mongoengine.IntField(required=True)
    bookings = mongoengine.EmbeddedDocumentListField(Booking)

    meta = {
        'db_alias': 'core',
        'collecition': 'rooms'
    }
