from typing_extensions import Required
import mongoengine
import datetime
from schema.bookings import Booking


class Guest(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)

    name = mongoengine.StringField(required=True)
    surname = mongoengine.StringField(required=True)
    email = mongoengine.StringField(required=True)

    bookings = mongoengine.EmbeddedDocumentListField(Booking)

    meta = {
        'db_alias': 'core',
        'collection': 'guests'
    }
