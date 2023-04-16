import json
import re
import traceback
from datetime import timedelta

from apps.utils.logger import get_logger


def parse_time(time_str):
    """
    Parse a time string e.g. (2h13m) into a timedelta object.

    Modified from virhilo's answer at https://stackoverflow.com/a/4628148/851699

    :param time_str: A string identifying a duration.  (eg. 2h13m)
    :return datetime.timedelta: A datetime.timedelta object
    """
    regex = re.compile(
        r'^((?P<days>[\.\d]+?)d)?((?P<hours>[\.\d]+?)h)?((?P<minutes>[\.\d]+?)m)?((?P<seconds>[\.\d]+?)s)?$')
    parts = regex.match(time_str)
    assert parts is not None, "Could not parse any time information from '{}'.  Examples of valid strings: '8h', " \
                              "'2d8h5m20s', '2m4s'".format(
        time_str)
    time_params = {name: float(param) for name, param in parts.groupdict().items() if param}
    return timedelta(**time_params)


def load_json_file(file_path):
    logger = get_logger('load_json_file')
    data = []
    try:
        fopen = open(file_path)
        data = json.load(fopen)
        fopen.close()
    except Exception as e:
        logger.error(f'Failed to read file: {e}')
        logger.error(traceback.format_exc())
    return data
