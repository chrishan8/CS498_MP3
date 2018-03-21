import happybase as hb

connection = hb.Connection()

table = connection.table('powers')
row1 = table.row(b'row1')
row19 = table.row(b'row19')

print('hero: {}, power: {}, name: {}, xp: {}, color: {}'.format(row1[b'personal:hero'], row1[b'personal:power'], row1[b'professional:name'], row1[b'professional:xp'], row1[b'custom:color']))
print('hero: {}, color: {}'.format(row19[b'personal:hero'], row19[b'custom:color']))
print('hero: {}, name: {}, color: {}'.format(row1[b'personal:hero'], row1[b'professional:name'], row1[b'custom:color']))
