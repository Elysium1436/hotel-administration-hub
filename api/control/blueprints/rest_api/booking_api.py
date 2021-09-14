from flask_restx import Resource, Namespace, fields


api = Namespace("Booking Interface")

booking_fields = {
    "guest_id": fields.String(attribute="guest.id"),
    "booked_date": fields.DateTime(),
    "checkin": fields.DateTime(),
    "checkout": fields.DateTime(),
    "total_price": fields.Float(),
    "room_name": fields.String(attribute="room.room_name"),
    "status": fields.String(),
}
