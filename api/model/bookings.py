import mongoengine
import datetime
from api.service.guest_service import find_guest


class Booking(mongoengine.Document):

    guest = mongoengine.ReferenceField("Guest", required=True)

    booked_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    checkin = mongoengine.DateTimeField(required=True)
    checkout = mongoengine.DateTimeField(required=True)
    total_price = mongoengine.FloatField(required=True)
    room = mongoengine.ReferenceField("Room", required=True)
    status = mongoengine.StringField(default="unconfirmed", required=True)

    @property
    def total_days(self):
        dt = self.checkout_date - self.checkin_date
        return dt.days

    def guest_by_email(self, email, return_instance=False):
        guest = find_guest(email)
        self.guest = guest

        if return_instance:
            return guest
