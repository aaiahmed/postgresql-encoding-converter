"""
Copies a PostgreSQL table encoded in SQL_ASCII,
converts to UTF-8 encoding and loads into a new schema for review.
"""
from utils.config import get_config
from utils.query import unload_table, load_table
from utils.convert import convert_to_utf8


def convert_table_encoding():
    """
    Converts a list of postgres tables from sql_ascii to utf-8.
    :return:
    """

    conf = get_config()
    src_tables = conf['postgres']['src_tables']
    dst_tables = conf['postgres']['dst_tables']

    for i, table in enumerate(src_tables):
        unload_table(table, conf)
        convert_to_utf8(table, conf)

        if conf['app']['load']:
            load_table(dst_tables[i], conf)


def main():
    convert_table_encoding()


if __name__ == '__main__':
    main()
