from flask_restx import Resource, Namespace, fields
from flask import request, abort, make_response
from flask_restx.marshalling import make
from marshmallow.decorators import post_load, validates_schema, pre_load
from marshmallow import Schema, fields, ValidationError
from api.service import room_service, guest_service, booking_service
from api.model import bookings
from pprint import pprint

api = Namespace("test", path="/test")

