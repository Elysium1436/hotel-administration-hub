from api.service import role_service
from flask_restx import Namespace, fields, Resource
from flask import request

api = Namespace("Role Namespace", path="/role")

role_fields = {
    "role_name": fields.String(),
    "permissions": fields.List(fields.String()),
}
role_model = api.model("Role", role_fields)

roles_fields = {"roles": fields.List(fields.Nested(role_fields))}

roles_model = api.model("Roles", roles_fields)


@api.route("/")
class Role(Resource):
    @api.marshal_with(roles_model)
    def get(self):
        roles = role_service.get_all_roles()
        return {"roles": roles}

    def post(self):
        role_service.add_role(**request.json)

    def delete(self):
        role_service.wipe_roles()
