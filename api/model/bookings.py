from typing_extensions import Required
import mongoengine
import datetime


class Booking(mongoengine.Document):

    guest = mongoengine.ReferenceField('Guest', required=True)

    booked_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    checkin = mongoengine.DateTimeField(required=True)
    checkout = mongoengine.DateTimeField(required=True)
    total_price = mongoengine.FloatField(required=True)
    room = mongoengine.ReferenceField(required=True)
    status = mongoengine.StringField(default='unconfirmed', required=True)

    @property
    def total_days(self):
        dt = self.checkout_date - self.checkin_date
        return dt.days
