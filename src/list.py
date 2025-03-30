from pathlib import Path

import click
from cli import cli

@cli.command()
@click.argument(
    'location',
    type=click.Path(exists=True),
    default = Path('.')
)
def list(**kwargs):
    print(kwargs['location'].glob('*'))
    