"""
Unloads a table into temp folder as csv.
"""

from utils.execute import execute
from utils.command import get_unload_command


def unload_table(conf, table):
    """
    Unloads the given table.
    :param conf: config as dictionary.
    :param table: table name.
    :return:
    """

    command = get_unload_command(conf, table)
    result = execute(command)
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
