from api.service import guest_service
from flask_restx import Resource, Namespace, fields
from .booking_api import booking_fields

api = Namespace("Guest Interface", "Opens the interface for guest manipulations")

guest_fields = {
	"name":fields.String(),
	"surname":fields.String(),
	"email":fields.String(),
	"registered_date":fields.DateTime(),
	"bookings":fields.List(fields.Nested(booking_fields))
}

guest_model = api.model("Guest Model", guest_fields)

class Guest(Resource):
	def get(self):
		pass
	def post(self):
		pass
	def delete(self):
		pass