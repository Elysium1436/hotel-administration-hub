import click
from schema.roles import Permission


def permissions():
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
