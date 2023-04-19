import os

APP_SECRET = JWT_SECRET = os.environ['APP_SECRET']

FIXTURES_DIR = 'config/fixtures'

SECURITY_PASSWORD_HASH = os.environ['SECURITY_PASSWORD_HASH']
SECURITY_PASSWORD_SALT = os.environ['SECURITY_PASSWORD_SALT']
SECURITY_PASSWORD_COMPLEXITY_CHECKER = os.environ['SECURITY_PASSWORD_COMPLEXITY_CHECKER']
SECURITY_REGISTERABLE = os.environ['SECURITY_REGISTERABLE'] == 'True'
SECURITY_RECOVERABLE = os.environ['SECURITY_RECOVERABLE'] == 'True'

SECURITY_SEND_REGISTER_EMAIL = os.environ['SECURITY_SEND_REGISTER_EMAIL'] == 'True'
SECURITY_USERNAME_ENABLE = os.environ['SECURITY_USERNAME_ENABLE'] == 'True'

JWT_ACCESS_TOKEN_EXPIRES = os.environ['JWT_ACCESS_TOKEN_EXPIRES']
JWT_REFRESH_TOKEN_EXPIRES = os.environ['JWT_REFRESH_TOKEN_EXPIRES']

DB_HOST = os.environ['DATABASE_HOST']
DB_PORT = os.environ['DATABASE_PORT'] or '5432'
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_NAME = os.environ['DATABASE_NAME']

MAIL_SERVER = os.environ.get('MAIL_SERVER')
MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') == 'True'
MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') == 'True'
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

ADMINS = ['your-email@example.com']

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
}
