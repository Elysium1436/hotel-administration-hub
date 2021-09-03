import mongoengine
import datetime


class Booking(mongoengine.EmbeddedDocument):

    guest_id = mongoengine.ObjectIdField(required=True)

    booked_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    checkin_date = mongoengine.DateTimeField(required=True)
    checkout_date = mongoengine.DateTimeField(required=True)
    total_price = mongoengine.FloatField(required=True)
    is_payed = mongoengine.BooleanField(default=False)

    @property
    def total_days(self):
        dt = self.checkout_date - self.checkin_date
        return dt.days
