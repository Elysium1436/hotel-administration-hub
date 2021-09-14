from api.service import user_service
from api.service.user_service import get_all_users
import api.service
from flask import Blueprint, request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token, get_current_user, jwt_required
from .api_utils import jwt


api = Namespace("user namespace", "The user interaction interface.")


user_fields = {
    "id": fields.String(),
    "username": fields.String(),
    "email": fields.String(),
    "registered_date": fields.DateTime(),
    "role_name": fields.String(attribute=lambda x: x.role.role_name),
    "permissions": fields.List(fields.String(attribute=lambda x: x.role.permissions)),
}
user_model = api.model("User", user_fields)


multiple_user_fields = {"users": fields.List(fields.Nested(user_model))}
users_model = api.model("Users", multiple_user_fields)


@api.route("/")
class Users(Resource):
    @api.marshal_with(users_model)
    def get(self):
        return {"users": user_service.get_all_users()}

    @api.marshal_with(user_model)
    def post(self):
        return user_service.add_user(return_instance=True, **request.json)

    def delete(self):
        user_service.wipe_users()
        return {"message": "Yikes..."}


@api.route("/email/<email>")
class UserFromEmail(Resource):
    @api.marshal_with(user_model)
    def get(self, email):
        return user_service.find_user_by_email(email)


@api.route("/username/<username>")
class UserFromUsername(Resource):
    @api.marshal_with(user_model)
    def get(self, username):
        return user_service.find_user_by_username(username)
