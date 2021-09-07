from .dataservice_utils import table_print_schema
from ..model.guests import Guest


def add_guest(name, surname, email, return_instance=False):
    guest = Guest()
    guest.name = name
    guest.surname = surname
    guest.email = email

    guest.save()

    if return_instance:
        return guest


def find_guest(email):
    guest = Guest.objects(email=email).first()
    if guest is None:
        raise ValueError(f"Guest with email \"{email}\" doesn't exist.")
    return guest


def view_guests():
    guests = Guest.objects().all()
    table_print_schema(Guest, ['name', 'surname', 'email', 'password_hash'])


def delete_guest(email):
    guest = Guest.objects(email=email).first()
    guest.delete()
