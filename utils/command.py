"""
Generates the psql shell command.
"""


def get_unload_command(table, conf):
    """
    Returns the shell command.
    :param table: table name.
    :param conf: config as dictionary.
    :return: shell command.
    """
    host = conf['postgres']['host']
    port = conf['postgres']['port']
    database = conf['postgres']['database']
    user = conf['postgres']['user']
    delimiter = conf['postgres']['delimiter']
    unload_qry = conf['postgres']['unload_qry'].format(
        table=table, filepath='temp/{table}.csv'.format(table=table), delimiter=delimiter)
    return ["psql", "-h", host, "-p", port, "-U", user, "-d", database, "-c", unload_qry]
