from ..config import TestingConfig
import mongoengine
from api.service import booking_service, guest_service, role_service, room_service, user_service
import pytest
import os
from ..config import TestingConfig
from ..model import bookings, guests, roles, rooms, users
from ..model.roles import Permission
import datetime


@pytest.fixture(scope='module')
def init_db():
    mongoengine.connect(TestingConfig.DB_NAME, host=TestingConfig.HOST)


def test_add_role(init_db):
    role = roles.Role(role_name='admin', permissions=[
                      Permission.USER, Permission.ROOM, Permission.GUEST, Permission.ROLE, Permission.BOOKING])
    role.save()

    role = roles.Role.objects(role_name='admin').first()

    assert role.role_name == 'admin'
    for permission in Permission:
        assert permission.value in role.permissions

    role.delete()


@pytest.fixture()
def fix_role(init_db):
    role = roles.Role(role_name='admin', permissions=[
                      Permission.USER, Permission.ROOM, Permission.GUEST, Permission.ROLE, Permission.BOOKING])
    role.save()
    yield role
    role.delete()


@pytest.mark.parametrize('username,email,password,role_name', [('elywely', 'randomemail123@Gmail.com', 'password123', 'admin')])
def test_insert_user(fix_role, username, email, password, role_name):
    user_service.add_user(
        username, email, password, role_name)

    user = user_service.find_user(email)
    assert user.username == username
    assert user.email == email
    assert user.verify_password(password)
    assert user.role.role_name == role_name
    user.delete()


@pytest.fixture(params=[('elywely', 'randomemail123@Gmail.com', 'password123', 'admin')])
def fix_user(insert_role, request):
    username, email, password, role_name = request.param
    user = user_service.add_user(username, email, password, role_name)
    yield user
    user.delete()


@pytest.mark.parametrize('name,surname,email', [('John', 'Smith', 'johnsmith123@gmail.com')])
def test_insert_guest(init_db, name, surname, email):
    guest_service.add_guest(name, surname, email)
    guest = guest_service.find_guest(email)
    assert guest.name == name
    assert guest.surname == surname
    assert guest.email == email
    guest.delete()


@pytest.fixture(params=[('John', 'Smith', 'johnsmith123@gmail.com')])
def fix_guest(init_db, request):
    name, surname, email = request.params
    guest = guest_service.add_guest(name, surname, email, return_instance=True)
    yield guest
    guest.delete()


today = datetime.datetime.now()
tomorrow = today+datetime.timedelta(days=1)
r = room_service.Room('itsaroom', 69)

booking_params = [(today, tomorrow, 400.69, r, 'confirmed')]


@pytest.mark.parametrize('checkin,checkout,total_price,room,status', booking_params)
def insert_booking(fix_guest, checkin, checkout, total_price, room, status):
    booking = booking_service.add_booking(
        fix_guest, checkin, checkout, total_price, room, status)
    booking.save()
    booking = booking_service.find_booking(id=booking.id).first()

    assert booking.guest.name == fix_guest.name
    assert booking.checkin == checkin
    assert booking.checkout == checkout
    assert booking.total_price == total_price
    assert booking.status == status

    booking.delete()


@pytest.fixture(params=booking_params)
def fix_booking(request):
    fix_guest, checkin, checkout, total_price, status = request.params
    booking = booking_service.Booking(
        guest=fix_guest, checkin=checkin, checkout=checkout, total_price=total_price, status=status)
    booking.save()
    yield booking
    booking.delete()


@pytest.mark.parametrize('room_name,max_people,bookings', )
def test_insert_room(fix_booking):
