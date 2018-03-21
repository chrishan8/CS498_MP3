import happybase as hb
import re

connection = hb.Connection()

for table in connection.tables():
    print(re.sub("[\'b]", "", str(table)))

connection.close()
