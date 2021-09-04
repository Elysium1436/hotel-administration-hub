from enum import unique
import mongoengine
import datetime

from werkzeug.security import check_password_hash, generate_password_hash
from .bookings import Booking
from mongoengine import ReferenceField


class Guest(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)

    name = mongoengine.StringField(required=True)
    surname = mongoengine.StringField(required=True)
    email = mongoengine.EmailField(required=True, unique=True)
    password_hash = mongoengine.StringField(required=True)
    bookings = mongoengine.ListField(ReferenceField(Booking))

    @property
    def password(self):
        raise AttributeError("Cannot access guest password")

    @password.setter
    def password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    bookings = mongoengine.ListField(ReferenceField(Booking))

    meta = {
        'db_alias': 'core',
        'collection': 'guests'
    }
