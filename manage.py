import os
import traceback
from importlib import import_module

import click
from flask.cli import FlaskGroup

from apps import consts
from app import create_app
from apps.shared.models import db
from apps.utils.helpers import load_json_file
from apps.utils.logger import get_logger

cli = FlaskGroup(create_app=create_app)


@cli.command('test')
@click.argument('test_case', default='test')
def test(test_case='test'):
    logger = get_logger('test')
    logger.error(f'Hello {test_case}')


@cli.command('seed')
def seed():
    logger = get_logger('seed')
    for filename in os.listdir(consts.FIXTURES_DIR):
        data = load_json_file(f'config/fixtures/{filename}')
        for model_data in data:
            try:
                module, class_name = model_data['model'].rsplit('.', 1)
                klass = getattr(import_module(module), class_name)
                for record in model_data['records']:
                    model_instance = klass(**record)
                    db.session.add(model_instance)
                db.session.commit()
            except Exception as e:
                logger.error(e)
                logger.error(traceback.format_exc())


if __name__ == '__main__':
    cli()
