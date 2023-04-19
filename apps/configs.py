from apps import consts
from apps.utils.helpers import parse_time


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = consts.APP_SECRET
    JWT_SECRET_KEY = consts.JWT_SECRET

    SECURITY_PASSWORD_HASH = consts.SECURITY_PASSWORD_HASH
    SECURITY_PASSWORD_SALT = consts.SECURITY_PASSWORD_SALT
    SECURITY_PASSWORD_COMPLEXITY_CHECKER = consts.SECURITY_PASSWORD_COMPLEXITY_CHECKER
    SECURITY_REGISTERABLE = consts.SECURITY_REGISTERABLE
    SECURITY_SEND_REGISTER_EMAIL = consts.SECURITY_SEND_REGISTER_EMAIL
    SECURITY_USERNAME_ENABLE = consts.SECURITY_USERNAME_ENABLE
    SECURITY_RECOVERABLE = consts.SECURITY_RECOVERABLE

    JWT_ACCESS_TOKEN_EXPIRES = parse_time(consts.JWT_ACCESS_TOKEN_EXPIRES)
    JWT_REFRESH_TOKEN_EXPIRES = parse_time(consts.JWT_REFRESH_TOKEN_EXPIRES)

    MAIL_SERVER = consts.MAIL_SERVER
    MAIL_PORT = consts.MAIL_PORT
    MAIL_USE_TLS = consts.MAIL_USE_TLS
    MAIL_USE_SSL = consts.MAIL_USE_SSL
    MAIL_USERNAME = consts.MAIL_USERNAME
    MAIL_PASSWORD = consts.MAIL_PASSWORD
    ADMINS = consts.ADMINS

    SQLALCHEMY_DATABASE_URI = \
        f"postgresql://{consts.DB_USER}:{consts.DB_PASSWORD}@{consts.DB_HOST}:{consts.DB_PORT}/{consts.DB_NAME}"


class Production(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
