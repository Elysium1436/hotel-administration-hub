from .dataservice_utils import table_print_schema
from ..model.guests import Guest


def add_guest(name, surname, email, return_instance=False):
    guest = Guest()
    guest.name = name.lower()
    guest.surname = surname.lower()
    guest.email = email

    guest.save()

    if return_instance:
        return guest


def find_guest(**kwargs):
    guest = Guest.objects(**kwargs).first()
    return guest


def get_all_guests():
    return Guest.objects.all()


def view_guests():
    table_print_schema(Guest, ["name", "surname", "email"])


def wipe_guests():
    Guest.objects().delete()


def delete_guest(email):
    guest = Guest.objects(email=email).first()
    guest.delete()
