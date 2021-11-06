from flask_restx import ValidationError


class FieldValidationError(ValidationError):
    def __init__(self, msg, field_msgs={}, *args, **kwargs):
        self.field_msgs = field_msgs
        super().__init__(msg, *args, **kwargs)
