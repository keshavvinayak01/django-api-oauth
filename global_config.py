import configparser
import io


def get_global_config():
    config = configparser.ConfigParser()
    config.read('global_config.ini')
    return config