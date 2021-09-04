from src.schema.rooms import Room
from src.schema.guests import Guest
from src.schema.bookings import Booking
from tabulate import tabulate
from .users import User
from .roles import Role, Permission
from typing import List
import click


def table_print_schema(cls, columns):
    objs = cls.objects().all()
    table = [[str(getattr(obj, col)) for col in columns] for obj in objs]
    click.echo(tabulate(table, headers=columns))


def add_user(name, email, password, role_name):
    user = User()
    user.username = name
    user.email = email
    user.password = password
    role = Role.objects(role_name=role_name).first()
    print(role)
    user.roles = [role]

    user.save()


def print_users():
    table_print_schema(User, ['username', 'email', 'password_hash'])


def delete_user(username, email):
    user = User.objects(username=username).first()
    user.delete()


def add_role(role_name, permissions: List[Permission]):
    role = Role()
    role.role_name = role_name
    role.permissions = permissions

    role.save()


def print_roles():
    table_print_schema(Role, ['role_name', 'permissions'])


def delete_role(role_name):
    role = Role.objects(role_name=role_name)
    role.delete()


def add_booking(guest, date_in, date_out, total_price, status='unconfirmed'):
    booking = Booking()
    booking.guest = guest
    booking.checkin_date = date_in
    booking.checkout_date = date_out
    booking.total_price = total_price
    booking.status = 'unconfirmed'


def view_bookings():
    bookings = Booking.objects().all()
    table_print_schema(
        bookings, ['checkin_date', 'checkout_date', 'total_price', 'status'])


def add_guest(name, surname, email, password):
    guest = Guest()
    guest.name = name
    guest.surname = surname
    guest.email = email
    guest.password = password

    guest.save()


def view_guests():
    guests = Guest.objects().all()
    table_print_schema(Guest, ['name', 'surname', 'email', 'password_hash'])


def delete_guest(email):
    guest = Guest.objects(email=email).first()
    guest.delete()


def add_room(room_name, max_people):
    room = Room()
    room.room_name = room_name
    room.max_people = max_people

    room.save()


def view_rooms():
    rooms = Room.objects().all()
    table_print_schema(Room, ['room_name', 'max_people'])


def delete_room(room_name):
    room = Room.objects(room_name=room_name).first()
    room.delete()
