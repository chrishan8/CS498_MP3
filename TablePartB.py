import happybase as hb

connection = hb.Connection()

print(connection.tables())

for table in connection.tables():
    print(table.split("'")[1])

connection.close()
