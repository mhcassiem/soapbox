import consts


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = consts.APP_SECRET
    JWT_SECRET_KEY = consts.JWT_SECRET
    JWT_ACCESS_TOKEN_EXPIRES = consts.JWT_ACCESS_TOKEN_EXPIRES
    JWT_REFRESH_TOKEN_EXPIRES = consts.JWT_REFRESH_TOKEN_EXPIRES

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
