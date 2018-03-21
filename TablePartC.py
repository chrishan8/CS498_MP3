import happybase as hb
import csv

connection = hb.Connection()

table = connection.table('powers')
with open('input.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        [rowId, hero, power, name, xp, color] = list(map(lambda x: x.encode(), row))
        data = {
            b'personal:hero': hero,
            b'personal:power': power,
            b'professional:name': name,
            b'professional:xp': xp,
            b'custom:color': color
        }
        table.put(rowId, data)

connection.close()
