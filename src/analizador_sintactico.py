from analizador_lexico import AnalizadorLexico
from gramatica import SeparadorGramatica

class AnalizadorSintactico:

    def __init__(self):
        self.gramatica = SeparadorGramatica()
        self.lexico = AnalizadorLexico()
        self.matriz = [
            [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6],
            [7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 11, 12, 13, 14, 15, 16, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 19, 20, 21, 22, 23, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 25, 26, 27, 28, 29, 0]
        ]

    def lldriver(self):
        if len(self.lexico.tabla_errores) > 0:
            return

        no_terminales = self.gramatica.no_terminales
        # terminales = self.gramatica.terminales
        stack = []
        stack.append('inicio')
        x = stack[0]
        a = self.lexico.siguiente()
        vacio = 'E'

        while len(stack) > 0:
            x = stack[len(stack) - 1]
            if x in no_terminales:
                if self.predict(x, a) != 0:
                    produccion = self.gramatica.get_produccion(self.predict(x, a) - 1)
                    x = produccion[0]
                    stack.pop()
                    # Ciclo de push
                    produccion.reverse()
                    for element in produccion:
                        stack.append(element)
                else:
                    print('Error de sintáxis 1')
                    return
            else:
                if x == vacio:
                    stack.pop()
                elif x == a:
                    stack.pop()
                    a = self.lexico.siguiente()
                    if a == '$':
                        break
                else:
                    print('Error de sintáxis 2')
                    return
        print('Sintáxis correcta')

    def predict(self, x, a):
        return self.matriz[self.gramatica.no_terminales.index(x)][self.gramatica.terminales.index(a)]

def main():
    asintactico = AnalizadorSintactico()
    asintactico.lldriver()

if __name__ == '__main__':
    main()

