from ..model.users import User
from .dataservice_utils import table_print_schema


def add_user(username, email, password, role, return_instance=False):
    user = User()
    user.username = username
    user.email = email
    user.password = password
    user.role = role

    user.save()
    if return_instance:
        user = find_user_by_email(email)
        return user


def get_all_users():
    return User.objects().all()


def find_user(**kwargs):
    d = {
        "id": find_user_by_id,
        "username": find_user_by_username,
        "email": find_user_by_email,
    }
    field, value = kwargs.items()[0]
    return d[field](value)


def find_user_by_id(id: int):
    user = User.objects(id=id).first()
    return user


def find_user_by_username(username: str):
    return User.objects(username=username).first()


def find_user_by_email(email: str):
    return User.objects(email=email).first()


def view_users():
    table_print_schema(User, ["username", "email", "password_hash"])


def delete_user(email):
    user = User.objects(email=email).first()
    user.delete()


def wipe_users():
    User.objects().delete()
