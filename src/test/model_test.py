from ..config import TestingConfig
import mongoengine
from ..service import booking_service, guest_service, role_service, room_service, user_service
import pytest
import os
from ..config import TestingConfig
from model import bookings, guests, roles, rooms, users
from model.roles import Permission


@pytest.fixture(scope='module')
def init_db():
    mongoengine.connect(hostname=TestingConfig.HOST)
    yield
    mongoengine.disconnect()


def test_add_role(init_db):
    role = roles.Role(role_name='admin', permissions=[
                      Permission.USER, Permission.ROOM, Permission.GUEST, Permission.ROLE, Permission.BOOKING])
    role.save()

    role = roles.Role.objects(role_name='admin')

    assert role.name == 'admin'
    for permission in Permission:
        assert permission in role.permissions


@pytest.fixture()
def insert_role():
    role = roles.Role(role_name='admin', permissions=[
                      Permission.USER, Permission.ROOM, Permission.GUEST, Permission.ROLE, Permission.BOOKING])
    role.save()
    yield role
    role.delete()


@pytest.mark.parametrize('username,email,password,role_name', [('elywely', 'bryan.af7@Gmail.com', 'password123', 'admin')])
def test_insert_user(init_db, username, email, password, role_name):
    user_service.add_user(
        username, email, password, role_name)

    user = user_service.find_user(email)
    assert user.name == username
    assert user.email == email
    assert user.verify_password(password)
    assert user.role.role_name == role_name
