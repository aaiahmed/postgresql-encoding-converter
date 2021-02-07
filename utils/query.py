"""
Queries database to unload and load table.
"""

from utils.execute import execute
from utils.command import get_unload_command, get_load_command, get_ddl_command
from utils.logger import get_logger

logger = get_logger()


def unload_table(table, conf):
    """
    Unloads the given table as csv.
    :param table: table name.
    :param conf: config as dictionary.
    :return:
    """

    logger.info('Exporting source table: "{table}" into CSV from source database...'.format(table=table))
    command = get_unload_command(table, conf)
    result = execute(command)
    logger.debug(result.stdout)
    if result.returncode != 0:
        raise RuntimeError(result.stderr)


def create_table(table, conf):
    """
    Creates the destination table.
    :param table: table name.
    :param conf: config as dictionary.
    :return:
    """

    logger.info('Creating target table: "{table}" in destination database...'.format(table=table))
    command = get_ddl_command(table, conf)
    result = execute(command)
    logger.debug(result.stdout)
    if result.returncode != 0:
        raise RuntimeError(result.stderr)


def load_table(table, conf):
    """
    Loads the given table from csv.
    :param table: table name.
    :param conf: config as dictionary.
    :return:
    """

    logger.info('Loading converted CSV into destination table: "{table}" in target database...'.format(table=table))
    command = get_load_command(table, conf)
    result = execute(command)
    logger.debug(result.stdout)
    if result.returncode != 0:
        raise RuntimeError(result.stderr)