import mongoengine
import datetime
from mongoengine import ReferenceField


class Guest(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    surname = mongoengine.StringField(required=True)
    email = mongoengine.EmailField(required=True, unique=True)
    bookings = mongoengine.ListField(ReferenceField("Booking"))
