import happybase as hb
import re

connection = hb.Connection()

print(connection.tables())

for table in connection.tables():
    print(re.sub("[\',b]", '', table))

connection.close()
