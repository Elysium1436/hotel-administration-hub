from marshmallow.exceptions import ValidationError
from api.model import roles
from marshmallow import Schema, fields, validate
from marshmallow.decorators import post_dump, post_load, pre_dump
from api.service import role_service
from flask_restx import Namespace, Resource
from flask import request

api = Namespace("Role Namespace", path="/role")


def permission_validator(permissions):
    def validator(values):
        print(values)
        if not all(v in permissions for v in values):
            raise ValidationError("One or more values do not belong here dumbass")

    return validator


class EnumField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if not value:
            return None
        #Sometimes mongoengine returns string for no reason other than to just spite me
        if isinstance(value,str):
            return value
        return value.name

    def _deserialize(self, value, attr, obj, **kwargs):
        if not value:
            return None
        print("Deserialize:", value)
        return roles.Permission[value]


class RoleSchema(Schema):
    id = fields.String()
    role_name = fields.String()
    permissions = fields.List(EnumField())
    max_people = fields.Integer()

    class Meta:
        ordered = True

    @post_load
    def load_role(self, data, **kwargs):
        return roles.Role(**data)

    def find_role(self, data, many=True, **kwargs):
        role_obj = roles.Role.objects(**data)
        if many:
            return self.dump(role_obj.all(), many=many)
        return self.dump(role_obj.first())


@api.route("/")
class Role(Resource):
    def get(self):
        d = dict(request.args)
        many = "many" in d
        d.pop("many")
        return RoleSchema().find_role(d, many=many)

    def post(self, many=False):
        role = RoleSchema().load(request.get_json())
        role.save()
        return RoleSchema().dump(role)

    def delete(self):
        role_service.wipe_roles()
