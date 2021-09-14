from enum import unique
import mongoengine
from .bookings import Booking
from mongoengine import ReferenceField


class Room(mongoengine.Document):
    room_name = mongoengine.StringField(required=True, unique=True)
    max_people = mongoengine.IntField()
    bookings = mongoengine.ListField(ReferenceField(Booking))
