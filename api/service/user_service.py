from .dataservice_utils import table_print_schema
from ..model.users import User


def add_user(name, email, password, role_name, return_instance=False):
    user = User()
    user.username = name
    user.email = email
    user.password = password
    user.set_role_by_name(role_name)

    user.save()
    if return_instance:
        return user


def find_user(email: str):
    user = User.objects(email=email).first()
    return user


def view_users():
    table_print_schema(User, ['username', 'email', 'password_hash'])


def delete_user(email):
    user = User.objects(email=email).first()
    user.delete()
