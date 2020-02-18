symbol_table = {}
symbol_table['a'] = { 'type': 'int', 'value': 12 }

key = 'b'
try:
    print(symbol_table[key])
except KeyError:
    print('Identifier not found!')