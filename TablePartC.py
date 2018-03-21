import happybase as hb
import csv

connection = hb.Connection()

table = connection.table('powers')
with open('input.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        values = row.split[',']
        [rowId, hero, power, name, xp, color] = values.map(lambda x: x.encode())
        data = {
            b'personal:hero': hero,
            b'personal:power': power,
            b'professional:name': name,
            b'professional:xp': xp,
            b'custom:color': color
        }
        table.put(rowId, data)

connection.close()   
