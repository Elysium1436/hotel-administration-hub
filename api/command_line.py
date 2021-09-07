from model.guests import Guest
import click
from service.database_setup import global_init
from cli_utils import permission_prompt
from service import guest_service, user_service, room_service, booking_service, role_service
import logging


logging.basicConfig(
    filename='./general.log',
    level=logging.DEBUG,
    format='{asctime} | {levelname} | {module} | {lineno} | {funcName} | {message}',
    style='{'
)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter(
    '{levelname} | {name} | {module} | {lineno} | {funcName} | {message}', style='{')
ch.setFormatter(formatter)
logging.getLogger('').addHandler(ch)

logger = logging.getLogger("cli")


@click.group(invoke_without_command=True)
def cli():
    global_init()
    return


@cli.command("add-user")
@click.option('--role-name', required=True, prompt="The name of the role")
@click.option('--username', required=True, prompt="Your Username")
@click.password_option()
@click.option('--email', required=True, prompt="Your email")
def add_user(username, email, password, role_name):
    """Adds a user to the Administration System"""
    user_service.add_user(username, email, password, role_name)


@cli.command()
@click.option('--role-name', prompt="The name of the role")
def add_role(role_name):
    """Adds a role ro the Database"""
    permissions = permission_prompt()
    role_service.add_role(role_name, permissions)


@cli.command()
@click.option("--guest-email", type=str, prompt="Guests email", required=True)
@click.option("--checkin", type=click.DateTime(formats=["%d/%m/%Y"]), prompt="Checkin date dd/mm/yy", required=True)
@click.option("--checkout", type=click.DateTime(formats=["%d/%m/%Y"]), prompt="Checkout date dd/mm/yy", required=True)
@click.option("--total-price", type=float, prompt="Total Price", required=True)
@click.option("--status", type=str, prompt="Initial Status", default="unconfirmed")
def add_booking(guest_email, checkin, checkout, total_price, status):
    """Adds a Booking to the Database. Needs an existing guest's email."""
    guest = Guest.objects(email=guest_email).first()
    booking_service.add_booking(guest, checkin, checkout, total_price, status)


@cli.command()
@click.option("--room-name", type=str, required=True)
@click.option("--max-people", type=int)
def add_room(room_name, max_people):
    """Adds a Room to the Database"""
    room_service.add_room(room_name, max_people)


@cli.command()
@click.option("--name", prompt="Guest Name", required=True, type=str)
@click.option("--surname", prompt="Guest Surname", required=True, type=str)
@click.option("--email", prompt="Guest Email", required=True, type=str)
def add_guest(name, surname, email):
    """Adds a Guest to the Database"""
    guest_service.add_guest(name, surname, email)


@cli.command()
def show_roles():
    role_service.view_roles()


@cli.command()
def show_users():
    user_service.view_users()


@cli.command()
def show_bookings():
    booking_service.view_bookings()


@cli.command()
def show_guests():
    guest_service.view_guests()


@cli.command()
def show_rooms():
    room_service.view_rooms()
