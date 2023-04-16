from logging import config, getLogger

from apps.consts import LOGGING_CONFIG


def configure_logger():
    config.dictConfig(LOGGING_CONFIG)


def get_logger(logger_name='logger'):
    configure_logger()
    return getLogger(logger_name)
