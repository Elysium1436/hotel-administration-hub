from dataservice_utils import table_print_schema
from model.guests import Guest


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
