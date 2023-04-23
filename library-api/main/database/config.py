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
    db_configs = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_configs[param[0]] = param[1]
    else:
        raise ValueError(f'Section {section} not found in the {filename} file')
    return db_configs
