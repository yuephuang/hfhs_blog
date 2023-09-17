import os

from config.envion import env_config


def get_config(key: str, default_value=None):
    if os.environ.get(key):
        return os.environ.get(key)
    elif env_config.get(key):
        return os.environ.get(key)
    else:
        return default_value

