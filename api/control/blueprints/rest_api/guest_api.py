from marshmallow import Schema, fields
from marshmallow.decorators import post_load
from api.service import guest_service
from flask_restx import Resource, Namespace
from flask import request
from api.model.guests import Guest

api = Namespace(
    "Guest Interface", "Opens the interface for guest manipulations", path="/guest"
)


class BookingSchema(Schema):
    id = fields.String()
    booked_date = fields.DateTime()
    checkin = fields.DateTime()
    checkout = fields.DateTime()
    total_price = fields.Float()
    room_name = fields.String(load_from="room.room_name")
    status = fields.String()


class GuestSchema(Schema):
    registered_date = fields.DateTime(dump_only=True)
    id = fields.String(dump_only=True)
    name = fields.String()
    surname = fields.String()
    email = fields.Email()
    bookings = fields.List(fields.Nested(BookingSchema()), dump_only=True)

    @post_load
    def load_guest(self, data, **kwargs):
        guest = Guest(**data)
        return guest

    def find_guest(self, data, many=True, **kwargs):
        guest = Guest.objects(**data)
        if many:
            return self.dump(guest.all(), many=many)
        return self.dump(guest.first())


@api.route("/")
class GuestResource(Resource):
    def get(self):
        d = dict(request.args)
        many = d.pop("many", None) is not None
        return GuestSchema().find_guest(d, many=many)

    def post(self):
        guest = GuestSchema().load(request.json)
        guest.save()
        return GuestSchema().dump(guest)

    def delete(self):
        guest_service.wipe_guests()
        return {"message": "Bruh..."}
