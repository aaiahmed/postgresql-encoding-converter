"""
Unloads a table into temp folder as csv.
"""

from utils.execute import execute
from utils.command import get_unload_command


def unload_table(table, conf):
    """
    Unloads the given table.
    :param table: table name.
    :param conf: config as dictionary.
    :return:
    """

    command = get_unload_command(table, conf)
    result = execute(command)
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
