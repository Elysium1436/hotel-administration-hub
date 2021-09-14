from flask_jwt_extended import JWTManager
import flask
from api.service.user_service import find_user_by_id

jwt = JWTManager()


@jwt.user_identity_loader
def user_identity_loader(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    id = jwt_data["sub"]
    return find_user_by_id(id)
