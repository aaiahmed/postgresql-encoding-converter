"""
Generates the psql shell command.
"""
import os
import psycopg2

def get_unload_command(table, conf):
    """
    Returns the shell command to unload a table.
    :param table: source table name.
    :param conf: config as dictionary.
    :return: shell command.
    """
    host = conf['postgres']['host']
    port = conf['postgres']['port']
    database = conf['postgres']['src_db']
    schema = conf['postgres']['src_schema']
    user = conf['postgres']['user']
    delimiter = conf['csv']['delimiter']
    unload_qry = conf['postgres']['unload_qry'].format(
        schema=schema, table=table, filepath='temp/{table}.csv'.format(table=table), delimiter=delimiter)
    return ["psql", "-h", host, "-p", port, "-U", user, "-d", database, "-c", unload_qry]


def get_load_command(table, conf):
    """
    Returns the shell command to load a table.
    :param table: destination table name.
    :param conf: config as dictionary.
    :return: shell command.
    """
    host = conf['postgres']['host']
    port = conf['postgres']['port']
    database = conf['postgres']['dst_db']
    schema = conf['postgres']['dst_schema']
    user = conf['postgres']['user']
    delimiter = conf['csv']['delimiter']
    load_qry = conf['postgres']['load_qry'].format(
        schema=schema, table=table, filepath='temp/{table}.converted.csv'.format(table=table), delimiter=delimiter)
    return ["psql", "-h", host, "-p", port, "-U", user, "-d", database, "-c", load_qry]


def get_ddl_command(table, conf):
    """
    Returns the shell command to get DDL create table statement for a table.
    :param table: source table name.
    :param conf: config as dictionary.
    :return: shell command.
    """
    host = conf['postgres']['host']
    port = conf['postgres']['port']
    database = conf['postgres']['dst_db']
    user = conf['postgres']['user']
    ddl_statement = get_ddl_statement(table, conf)
    return ["psql", "-h", host, "-p", port, "-U", user, "-d", database, "-c", ddl_statement]


def get_ddl_statement(table, conf):
    host = conf['postgres']['host']
    port = conf['postgres']['port']
    database = conf['postgres']['src_db']
    schema = conf['postgres']['src_schema']
    user = conf['postgres']['user']
    ddl_qry = conf['postgres']['ddl_qry'].format(schema=schema, table=table)

    try:
        conn = psycopg2.connect(host=host,
                                port=port,
                                database=database,
                                user=user,
                                password=os.getenv('PGPASSWORD'))
        cursor = conn.cursor()
        cursor.execute(ddl_qry)
        return cursor.fetchone()[0]
    except:
        pass
