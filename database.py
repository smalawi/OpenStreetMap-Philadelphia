import sqlite3
import csv
from pprint import pprint

db = sqlite3.connect('nodes_tags.csv')
c = db.cursor()

# Recreate table
c.execute('''DROP TABLE IF EXISTS nodes_tags''')
db.commit()

c.execute('''
    CREATE TABLE nodes_tags(id INTEGER, key TEXT, value TEXT,type TEXT)
''')
db.commit()

