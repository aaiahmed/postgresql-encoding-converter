"""
Reads config file and returns a dictionary.
"""
import yaml


def get_config():
    """
    Reads the config and returns as a dictionary.
    :return: config
    """

    with open('config.yaml') as file:
        return yaml.load(file, Loader=yaml.FullLoader)
