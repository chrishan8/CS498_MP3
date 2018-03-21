import happybase as hb
import re

connection = hb.Connection()

for table in connection.tables():
    print(table.decode("utf-8"))

connection.close()
