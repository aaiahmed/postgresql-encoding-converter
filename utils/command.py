"""
Generates the psql shell command.
"""


def get_unload_command(conf, table):
    """
    Returns the shell command.
    :param conf: config as dictionary.
    :param table: table name.
    :return: shell command.
    """
    host = conf['postgresql']['host']
    port = conf['postgresql']['port']
    database = conf['postgresql']['database']
    user = conf['postgresql']['user']
    delimiter = conf['postgresql']['delimiter']
    unload_qry = conf['postgresql']['unload_qry'].format(
        table=table, filepath='temp/{table}.csv'.format(table=table), delimiter=delimiter)
    return ["psql", "-h", host, "-p", port, "-U", user, "-d", database, "-c", unload_qry]


def main():
    """
    Main function.
    :return:
    """
    pass


if __name__ == '__main__':
    main()