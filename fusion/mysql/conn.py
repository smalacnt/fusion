"""establish mysql connection"""
import os
import MySQLdb

CONF_FILE = '/'.join((os.path.dirname(__file__), 'mysql.conf'))

DB = MySQLdb.connect(read_default_file=CONF_FILE)
