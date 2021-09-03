import click
from click.termui import hidden_prompt_func, prompt
from .schema.database_setup import global_init
from .schema.roles import Permission
import logging


def get_permissions():
    permissions = set()

    while True:
        perm = click.prompt(f"Add a permission (Added so far: {' '.join([str(i) for i in list(permissions)])})",
                            type=click.Choice(['perm1', 'perm2', 'perm3', 'exit'], case_sensitive=False), default='exit')

        if perm == 'exit':
            if not permissions:
                click.echo("Enter at least one permission")
                continue
            else:
                break

        permissions.add(Permission[perm])
    return list(permissions)


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


@click.group(invoke_without_command=True)
def cli():
    logger = logging.getLogger('main')
    logger.error('Something is in the way')
    global_init()
    return


@cli.command()
@click.argument('message')
def echo(message):
    click.echo(message)


@cli.command()
@click.option('--role-name', required=True, prompt="The name of the role")
@click.option('--permissions', required=True, prompt='The permissions of the role', multiple=True)
@cli.command()
@click.option('--username', required=True, prompt="Your Username")
@click.password_option()
@click.option('--email', required=True, prompt="Your email")
@click.option()
def add_user(username, password, email):
