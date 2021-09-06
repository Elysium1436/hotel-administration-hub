import click
from .model.roles import Permission


def permission_prompt():
    """Utility for prompting for multiple permissions."""
    permissions = set()

    while True:
        perm = click.prompt(f"Add a permission (Added so far: {' '.join([str(i) for i in list(permissions)])})",
                            type=click.Choice(['USER', 'GUEST', 'ROOM', 'ROLE', 'BOOKING', 'exit'], case_sensitive=False), default='exit')

        if perm == 'exit':
            if not permissions:
                click.echo("Enter at least one permission")
                continue
            else:
                break

        permissions.add(Permission[perm])
    return list(permissions)
