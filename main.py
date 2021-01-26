"""
Copies a PostgreSQL table encoded in SQL_ASCII,
converts to UTF-8 encoding and loads into a new schema for review.
"""
from utils.config import get_config
from utils.unload import unload_table


def main():
    conf = get_config()
    for table in conf['postgresql']['tables']:
        unload_table(conf, table)


if __name__ == '__main__':
    main()
