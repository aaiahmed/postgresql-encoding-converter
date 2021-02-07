"""
Returns logger.
"""
import logging.config
import yaml


def get_logger():
    """
    Returns logger.
    :return:
    """

    with open('logging.yaml', 'r') as file:
        conf = yaml.load(file, Loader=yaml.FullLoader)

    logging.config.dictConfig(conf)
    return logging.getLogger()