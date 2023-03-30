#!/usr/bin/python
import os
from configparser import ConfigParser

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
DATABASE_FILENAME = os.path.join(FILE_PATH, 'database.ini')

def config(filename=os.path.join(os.getcwd(),DATABASE_FILENAME), section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} not found in the {1} file'.format(section, filename))

    return db
