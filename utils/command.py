"""
Generates the psql shell command.
"""


def get_unload_command(table, conf):
    """
    Returns the shell command.
    :param table: source table name.
    :param conf: config as dictionary.
    :return: shell command.
    """
    host = conf['postgres']['host']
    port = conf['postgres']['port']
    database = conf['postgres']['src_db']
    user = conf['postgres']['user']
    delimiter = conf['csv']['delimiter']
    unload_qry = conf['postgres']['unload_qry'].format(
        table=table, filepath='temp/{table}.csv'.format(table=table), delimiter=delimiter)
    return ["psql", "-h", host, "-p", port, "-U", user, "-d", database, "-c", unload_qry]


def get_load_command(table, conf):
    """
    Returns the shell command.
    :param table: destination table name.
    :param conf: config as dictionary.
    :return: shell command.
    """
    host = conf['postgres']['host']
    port = conf['postgres']['port']
    database = conf['postgres']['dst_db']
    user = conf['postgres']['user']
    delimiter = conf['csv']['delimiter']
    load_qry = conf['postgres']['load_qry'].format(
        table=table, filepath='temp/{table}.converted.csv'.format(table=table), delimiter=delimiter)
    return ["psql", "-h", host, "-p", port, "-U", user, "-d", database, "-c", load_qry]