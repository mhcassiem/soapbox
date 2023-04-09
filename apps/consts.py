import os

from utils.helpers import parse_time


APP_SECRET = os.environ['APP_SECRET']
JWT_SECRET = os.environ['JWT_SECRET']
JWT_ACCESS_TOKEN_EXPIRES = parse_time(os.environ['JWT_ACCESS_TOKEN_EXPIRES'])
JWT_REFRESH_TOKEN_EXPIRES = parse_time(os.environ['JWT_REFRESH_TOKEN_EXPIRES'])

DB_HOST = os.environ['DATABASE_HOST']
DB_PORT = os.environ['DATABASE_PORT'] or '5432'
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_NAME = os.environ['DATABASE_NAME']
