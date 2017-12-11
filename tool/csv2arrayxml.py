""" Created by jieyi on 2017/12/08. """
import csv
import sys


def convert_csv_2_xml():
    file_path = None  # type: str
    if len(sys.argv) > 1:
        file_path = sys.argv[1]

    with open('arrays.xml', 'w+', encoding='utf-8-sig') as w:
        with open(file_path if file_path else 'arrays.csv', encoding='utf-8-sig') as f:
            array_type = ''
            w.write('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n')

            for row in csv.reader(f):
                # The each arrays.
                if 0 < len(row) and row[0]:
                    # Each item of the arrays.
                    if 1 < len(row) and 0 < len(row[1]):
                        # Here is title.
                        array_type = row[0]
                        w.write('\t<{}-array name="{}">\n'.format(array_type, row[1]))
                        continue
                    w.write('\t\t<item>{}</item>\n'.format(row[0]))
                elif 0 == len(row) or not any(row):
                    w.write('\t</{}-array>\n\n'.format(array_type))

        w.write('</resources>\n')


def main():
    convert_csv_2_xml()


if __name__ == '__main__':
    main()
