"""
Converts the raw unloaded file to uniform utf-8 encoding.
"""
import csv
import codecs


def read_csv(table, delimiter, error_handler):
    """
    Opens the unloaded csv and converts into utf-8 encoding,
    handling error (if any) with the configured error handler.
    :param table: Name of the table.
    :param delimiter: Delimiter.
    :param error_handler: Error handler, e.g. ignore, replace, backslashreplace. Refer to: https://docs.python.org/3/library/codecs.html#error-handlers
    :return:
    """
    with open('temp/{table}.csv'.format(table=table), errors=error_handler, encoding='utf-8') as f, \
            open('temp/{table}.converted.csv'.format(table=table), 'w') as fw:
        reader = csv.reader(f, delimiter=delimiter)
        writer = csv.writer(fw, delimiter=delimiter)
        for row in reader:
            row = [codecs.decode(item, 'unicode_escape') for item in row]
            writer.writerow(row)


def main():
    read_csv('raw.account', ',', 'backslashreplace')


if __name__ == '__main__':
    main()
