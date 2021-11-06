from .dataservice_utils import table_print_schema
from ..model.rooms import Room


def add_room(room_name, max_people, return_instance=False):
    room = Room()
    room.room_name = room_name
    room.max_people = max_people
    room.save()
    if return_instance:
        return room


def find_room(room_name):
    return Room.objects(room_name=room_name).first()


def get_all_rooms():
    return Room.objects().all()


def view_rooms():
    rooms = Room.objects().all()
    table_print_schema(Room, ["room_name", "max_people"])


def delete_room(room_name):
    room = Room.objects(room_name=room_name).first()
    room.delete()
