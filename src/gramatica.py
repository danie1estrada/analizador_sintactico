class SeparadorGramatica:

    def __init__(self):
        self.lado_derecho = []
        self.no_terminales = []
        self.terminales = []
        self.gramatica = []
        self.separar()

    def get_produccion(self, pos):
        produccion = self.lado_derecho[pos].split()
        return produccion

    def separar(self):
        separador = '>'
        vacio = 'E'

        with open('gramatica.txt') as grammar_file:
            for line in grammar_file:
                self.gramatica.append(line.strip())
                symbols = line.split()
                no_terminal = symbols.pop(0)

                if no_terminal not in self.no_terminales:
                    self.no_terminales.append(no_terminal)

                right_side = ''
                for symbol in symbols:
                    if symbol == separador:
                        continue
                    right_side += symbol + ' '
                self.lado_derecho.append(right_side.strip())

            for text in self.lado_derecho:
                symbols = text.split()

                for symbol in symbols:
                    if symbol in self.no_terminales:
                        continue
                    if symbol not in self.terminales and symbol != vacio:
                        self.terminales.append(symbol)