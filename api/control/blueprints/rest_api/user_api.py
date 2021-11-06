from marshmallow.exceptions import ValidationError
from api.model.roles import Role
from marshmallow.decorators import post_load, pre_load
from api.service import user_service
from api.service.user_service import get_all_users
import api.service
from flask import Blueprint, request
from flask_restx import Namespace, Resource
from flask_jwt_extended import create_access_token, get_current_user, jwt_required
from .api_utils import jwt
from marshmallow import fields, Schema
from api.service import role_service, user_service
from api.model import users

api = Namespace("user namespace", "The user interaction interface.")


class RoleSchema(Schema):
    id = fields.String()
    role_name = fields.String()
    permissions = fields.List(fields.String())

    @post_load
    def load_role(self, data, **kwargs):
        role = Role.objects(**data).first()
        if not role:
            raise ValidationError("No Role with those query data found.")
        return role


class UserSchema(Schema):
    registered_date = fields.DateTime(dump_only=True)
    id = fields.String(dump_only=True)
    username = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(load_only=True, required=True)
    role = fields.Nested(RoleSchema(), required=True)

    class Meta:
        ordered = True

    @post_load
    def load_user(self, data, **kwargs):
        user = users.User(**data)
        return user

    def find_user(self, data, many=True, **kwargs):
        users_obj = users.User.objects(**data)

        if many:
            return self.dump(users_obj.all(), many=many)
        return self.dump(users_obj.first())


@api.route("/")
class Users(Resource):
    def get(self):
        d = dict(request.args)
        many = True if d.pop("many", None) else False
        users = UserSchema().find_user(d, many=many)
        return users

    def post(self):
        data = request.get_json()
        user = UserSchema().load(data)
        user.save()
        return UserSchema().dump(user)

    def delete(self):
        user_service.wipe_users()
        return {"message": "Yikes..."}
