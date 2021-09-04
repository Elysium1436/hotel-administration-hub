import click
from click.termui import hidden_prompt_func, prompt
from .schema.database_setup import global_init
from .schema.roles import Role
from .cli_utils import permission_prompt
import logging
from .schema.database_utils import add_user, add_role, print_users, print_roles


# TODO add the other cli commands


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


@cli.command()
@click.argument('message')
def echo(message):
    click.echo(message)


@cli.command("add-user")
@click.option('--role-name', required=True, prompt="The name of the role")
@click.option('--username', required=True, prompt="Your Username")
@click.password_option()
@click.option('--email', required=True, prompt="Your email")
def add_user_db(username, email, password, role_name):
    add_user(username, email, password, role_name)


@cli.command()
@click.option('--role-name', prompt="The name of the role")
def add_role_db(role_name):
    permissions = permission_prompt()
    add_role(role_name, permissions)


@cli.command()
def show_roles():
    print_roles()


@cli.command()
def show_users():
    print_users()
