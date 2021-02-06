"""
Copies a PostgreSQL table encoded in SQL_ASCII,
converts to UTF-8 encoding and loads into a new schema for review.
"""
from utils.config import get_config
from utils.unload import unload_table
from utils.convert import convert_to_utf8


def convert_table_encoding():
    """
    Converts a list of postgres tables from sql_ascii to utf-8.
    :return:
    """

    conf = get_config()
    tables_for_conversion = conf['postgres']['source_tables']

    for table in tables_for_conversion:
        unload_table(table, conf)
        convert_to_utf8(table, conf)
        if conf['postgres']['load']:
            pass  # TODO: add postgres loader


def main():
    convert_table_encoding()


if __name__ == '__main__':
    main()
