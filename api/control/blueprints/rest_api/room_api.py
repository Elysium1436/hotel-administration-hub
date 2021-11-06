from api.model.bookings import Booking
from marshmallow.decorators import post_dump, post_load
from api.model import rooms
from flask_restx import Resource, Namespace
from flask import request
from marshmallow import Schema, fields
from api.service import room_service

api = Namespace("Room Api", path="/room")


class BookingSchema(Schema):
    id = fields.String()
    checkin = fields.DateTime()
    checkout = fields.DateTime()
    total_price = fields.Float()


class RoomSchema(Schema):
    id = fields.String()
    room_name = fields.String()
    max_people = fields.Integer()
    bookings = fields.List(fields.Nested(BookingSchema()), dump_only=True)

    @post_load
    def create_room(self, data, **kwargs):
        return rooms.Room(**data)

    def find_room(self, data, many=True, **kwargs):
        room = rooms.Room.objects(**data)
        if many:
            return self.dump(room.all(), many=many)
        return self.dump(room.first())


@api.route("/")
class Room(Resource):
    def get(self):
        d = dict(request.args)
        many = True if d.pop("many", None) else False
        return RoomSchema().find_room(d, many=many)

    def post(self):
        room = RoomSchema().load(request.get_json())
        room.save()
        return RoomSchema().dump(room)
