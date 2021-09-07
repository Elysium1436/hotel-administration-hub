from tabulate import tabulate
import click
import logging

logger = logging.getLogger(__name__)


def table_print_schema(cls, columns):
    objs = cls.objects().all()
    table = [[str(getattr(obj, col)) for col in columns] for obj in objs]
    click.echo(tabulate(table, headers=columns))
