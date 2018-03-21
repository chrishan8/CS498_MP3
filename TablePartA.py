import happybase as hb

connection = hb.Connection()
powersTable = connection.create_table('powers', {
    'personal': dict(),
    'professional': dict(),
    'custom': dict()
})

foodsTable = connection.create_table('food', {
    'nutrition': dict(),
    'taste': dict()
})

connection.close()
