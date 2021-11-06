from flask_restx import Api
from .user_api import api as user_ns
from .role_api import api as role_ns
from .booking_api import api as booking_ns
from .test_api import api as test_ns
from .room_api import api as room_ns
from .guest_api import api as guest_ns
from api.custom_errors import FieldValidationError

# TODO Return the instances on insertions
# TODO Maybe put role interface
# TODO Create properties based only easy unique values
api = Api(title="Hotel Api", description="Hotel Backend Api")


api.add_namespace(user_ns, path="/user")
api.add_namespace(role_ns)
api.add_namespace(booking_ns)
api.add_namespace(room_ns)
api.add_namespace(guest_ns)
api.add_namespace(test_ns)
