"""
Converts the raw unloaded file to uniform utf-8 encoding.
"""
import csv
import codecs


def convert_to_utf8(table, conf):
    """
    Opens the unloaded csv and converts into utf-8 encoding,
    handling error (if any) with the configured error handler.
    :param table: name of the table.
    :param conf: config as dictionary.
    :return:
    """

    delimiter = conf['csv']['delimiter']
    error_handler = conf['csv']['error_handler']

    with open('csv/{table}.csv'.format(table=table), errors=error_handler, encoding='utf-8') as f, \
            open('csv/{table}.converted.csv'.format(table=table), 'w') as fw:
        reader = csv.reader(f, delimiter=delimiter)
        writer = csv.writer(fw, delimiter=delimiter)
        for row in reader:
            row = [codecs.decode(item, 'unicode_escape') for item in row]
            writer.writerow(row)
