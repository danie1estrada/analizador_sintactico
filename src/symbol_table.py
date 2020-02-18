class SymbolTable:

    def __init__(self):
        self.symbol_table = []

    def insert(self):
        self.symbol_table.append({ 'identifier': '', 'type': 'int', 'value': 0 })

    def search(self, id):
        return next((item for item in self.symbol_table if item['identifier'] == id), None)

    def print(self):
        pass