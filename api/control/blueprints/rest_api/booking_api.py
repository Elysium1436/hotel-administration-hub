from flask_restx import Resource, Namespace, fields
from flask import request, abort, make_response
from flask_restx.marshalling import make
from marshmallow.decorators import post_load, validates_schema, pre_load
from marshmallow import Schema, fields, ValidationError
from api.service import room_service, guest_service, booking_service
from api.model import bookings
from pprint import pprint

api = Namespace("Booking", path="/booking")


# TODO Figure out auto documentation
# TODO format name/surname input and output
#
class GuestQuerySchema(Schema):
    id = fields.String()
    name = fields.String()
    surname = fields.String()
    email = fields.Email()

    @post_load
    def get_guest(self, data, **kwargs):
        guest = guest_service.find_guest(**data)
        if not guest:
            raise ValidationError({"guest": "No guest found"})
        return guest


class RoomQuerySchema(Schema):
    id = fields.String()
    room_name = fields.String()

    @post_load
    def get_room(self, data, **kwargs):
        room = room_service.find_room(**data)
        if not room:
            raise ValidationError({"room": "No room found"})
        return room


class BookingSchema(Schema):
    id = fields.String()
    booked_date = fields.DateTime()
    checkin = fields.DateTime()
    checkout = fields.DateTime()
    total_price = fields.Float()
    room = fields.Nested(RoomQuerySchema())
    guest = fields.Nested(GuestQuerySchema())

    class Meta:
        ordered = True

    @post_load
    def return_new_booking(self, data, **kwargs):
        return bookings.Booking(**data)

    def find_booking(self, data, first=True, **kwargs):
        books = bookings.Booking.objects(**data)
        if first:
            return self.dump(books.first())
        return self.dump(books.all(), many=True)


# dump transforms an object to dictionary
# load transform dictionary to object
@api.route("/")
class Booking(Resource):
    # success if extra info has been
    def post(self):
        body = request.get_json()
        booking = BookingSchema().load(body)
        booking.save()
        return BookingSchema().dump(booking)

    def get(self):
        r = dict(request.args)
        many = True if r.pop("many", False) else False
        bookings = BookingSchema().find_booking(r, first=many)
        return bookings
