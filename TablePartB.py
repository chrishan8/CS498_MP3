import happybase as hb
import re

connection = hb.Connection()

print(connection.tables())

for table in connection.tables():
    print(table)

connection.close()
