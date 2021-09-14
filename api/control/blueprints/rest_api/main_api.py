from flask_restx import Api
from .user_api import api as user_ns
from .role_api import api as role_ns


# TODO Return the instances on insertions

api = Api(title="Hotel Api", description="Hotel Backend Api")

api.add_namespace(user_ns, path="/user")
api.add_namespace(role_ns)
