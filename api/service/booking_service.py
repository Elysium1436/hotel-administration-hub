from .dataservice_utils import table_print_schema
from ..model.bookings import Booking


def add_booking(guest, checkin, checkout, total_price, room, status="unconfirmed", return_instance=True):
    booking = Booking()
    booking.guest = guest
    booking.checkin = checkin
    booking.checkout = checkout
    booking.total_price = total_price
    booking.status = status
    booking.room = room
    booking.save()
    if return_instance:
        return booking


def find_booking(booking_id, raise_on_empty=False):
    booking = Booking.objects(id=booking_id).first()
    if not booking and raise_on_empty:
        raise
    return Booking.objects(id=booking_id).first()


def get_all_bookings():
    return Booking.objects().all()


def view_bookings():
    table_print_schema(Booking, ["id", "checkin", "checkout", "total_price", "status"])
