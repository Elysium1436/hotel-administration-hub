from dataservice_utils import table_print_schema
from model.users import User
from model.roles import Role


def add_user(name, email, password, role_name):
    user = User()
    user.username = name
    user.email = email
    user.password = password
    role = Role.objects(role_name=role_name).first()
    user.roles = [role]

    user.save()


def view_users():
    table_print_schema(User, ['username', 'email', 'password_hash'])


def delete_user(username, email):
    user = User.objects(username=username).first()
    user.delete()
