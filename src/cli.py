import click
from pathlib import Path

@click.group()
def cli():
    pass

@cli.command()
@click.argument(
    'location',
    type=click.Path(exists=True),
    default = Path('.')
)
def list(**kwargs):
    found_objs = kwargs['location'].glob('*')
    for obj in found_objs:
        print(obj)
    

if __name__ == "__main__":
    cli()
