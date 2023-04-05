import click
from flask.cli import FlaskGroup

from app import create_app

cli = FlaskGroup(create_app=create_app)


@cli.command('test')
@click.argument('test_case', default='test')
def test(test_case='test'):
    print(f'Hello {test_case}')


if __name__ == '__main__':
    cli()
