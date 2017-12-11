""" Created by jieyi on 2017/12/08. """

import re

import sys


def convert_xml_2_csv():
    file_path = None  # type: str
    if len(sys.argv) > 1:
        file_path = sys.argv[1]

    with open(file_path if file_path else 'arrays.xml', encoding='utf-8-sig') as f, \
            open('arrays.csv', 'w+', encoding='utf-8-sig') as w:
        for row in f:
            if '-array name' in row:
                # array header
                regex = re.search(r'<(.*?)-array name="(.*?)"', row)
                data_type = regex.group(1)
                array_name = regex.group(2)
                w.write('{},{}\n'.format(data_type, array_name))
            elif '<item>' in row:
                # array body
                w.write('{}\n'.format(re.search(r'<item>(.*?)</item>', row).group(1)))
            elif re.match(r'.*?</(.*?)-array>', row):
                # array end
                w.write('\n')


if __name__ == '__main__':
    convert_xml_2_csv()
