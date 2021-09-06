from dataservice_utils import table_print_schema
from model.bookings import Booking


def add_booking(guest, date_in, date_out, total_price, status='unconfirmed'):
    booking = Booking()
    booking.guest = guest
    booking.checkin_date = date_in
    booking.checkout_date = date_out
    booking.total_price = total_price
    booking.status = status

    booking.save()


def view_bookings():
    bookings = Booking.objects().all()
    table_print_schema(
        bookings, ['checkin_date', 'checkout_date', 'total_price', 'status'])
