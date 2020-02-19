from data_table import DataTable
from table import Table

class AnalizadorLexico:

    def __init__(self):
        self.palabras_reservadas = (
            'boolean', 'int', 'float', 'double', 'char', 'void', 'public', 'private', 'protected', 'class', 'return',
            'import', 'new', 'if', 'else', 'for', 'while', 'const', 'extends', 'true', 'false', 'null', 'static'
        )
        self.caracteres_simples = (
            ',', ';', '.', ':', '{', '}', '[', ']', '(', ')', '&', '%', '+', '-', '*', '/', '!', '|', '=', '>', '<', '"', '\''
        )

        self.articulos = ('el', 'la', 'los', 'las')
        self.adjetivos = ('azul', 'horrible', 'enorme', 'blanco', 'negro', 'tonto')
        self.verbos = ('es', 'vive', 'corre', 'ladra', 'maulla', 'esta')

        self.tabla_palabras_reservadas = []
        self.tabla_simbolos = []
        self.tabla_errores = []
        self.tokens = []
        self.id = 400
        self.leer_archivo()

    def leer_archivo(self):
        # path = input('Escribe el nombre del archivo: ')
        with open('texto.txt') as programa_fuente:
            num_linea = 1
            for linea in programa_fuente:
                self.analizar(linea, num_linea)
                num_linea += 1

    def analizar(self, linea_actual, num_linea = 1):
        estado_actual = 0
        palabra = ''
        
        # Autómata
        i = 0
        while i < len(linea_actual):
            actual = linea_actual[i]
            # Ignora los espacios en blanco
            if str.isspace(actual) and estado_actual == 0:
                i += 1 
                continue
            # Estado inicial
            if estado_actual == 0:
                # Es un dígito
                if str.isdigit(actual):
                    estado_actual = 1
                    palabra += actual
                    i += 1
                # Es una letra
                elif str.isalpha(actual) or actual == '_' or actual == '$':
                    estado_actual = 6
                    palabra += actual
                    i += 1
                # Es caracter simple
                elif actual in self.caracteres_simples:
                    estado_actual = 0
                    palabra += actual
                    # print('Caracter:', palabra)
                    fila = {
                        'lexeme': palabra,
                        'token': 'special character',
                        'type': 'special character',
                        'value': ord(palabra)
                    }
                    # fila = ['Caracter simple', palabra, ord(palabra)]
                    # if fila not in self.tabla_simbolos:
                    self.tabla_simbolos.append(fila)
                    self.tokens.append(palabra)
                    palabra = ''
                    i += 1
            # Números
            elif estado_actual == 1:
                if str.isdigit(actual):
                    palabra += actual
                    i += 1
                # Punto flotante
                elif actual == '.':
                    estado_actual = 2
                    palabra += actual
                    i += 1
                # Caracter simple o espacio
                elif str.isspace(actual) or actual in self.caracteres_simples:
                    # Estado final
                    estado_actual = 0
                    # print('Número entero:', palabra)
                    fila = ['Número entero', palabra, 260]
                    fila = {
                        'lexeme': palabra,
                        'token': 'special character (number)',
                        'type': 'special character (number)',
                        'value': 270
                    }
                    # if fila not in self.tabla_simbolos:
                    self.tabla_simbolos.append(fila)
                    self.tokens.append(palabra)
                    palabra = ''
                # Error
                else:
                    estado_actual = -1
                    palabra += actual
                    i += 1
            # Estado 2
            elif estado_actual == 2:
                if str.isdigit(actual):
                    estado_actual = 3
                    palabra += actual
                    i += 1
                else:
                    estado_actual = -1
                    # palabra += actual
            # Estado 3
            elif estado_actual == 3:
                # print('3 -> ', end='')
                if str.isdigit(actual):
                    palabra += actual
                    i += 1
                elif str.isspace(actual) or actual in self.caracteres_simples:
                    estado_actual = 0
                    # print('Número de punto flotante:', palabra)
                    #fila = ['Número de punto flotante', palabra, 270]
                    fila = {
                        'lexeme': palabra,
                        'token': 'special character',
                        'type': 'special character',
                        'value': 270
                    }
                    # if fila not in self.tabla_simbolos:
                    self.tabla_simbolos.append(fila)
                    self.tokens.append(palabra)
                    palabra = ''
                else:
                    estado_actual = -1
                    palabra += actual
                    i += 1

            # Identificadores
            elif estado_actual == 6:
                if str.isalnum(actual) or actual == '_' or actual == '$':
                    palabra += actual
                    i += 1
                else:
                    estado_actual = 0
                    if palabra in self.palabras_reservadas:
                        # if [palabra] not in self.tabla_palabras_reservadas:
                        self.tabla_palabras_reservadas.append([palabra])
                        fila = {
                            'lexeme': palabra,
                            'token': 'keyword',
                            'type': 'keyword',
                            'value': 300
                        }
                        # self.id += 1
                        self.tabla_simbolos.append(fila)
                    else:
                        # identificador = ['Identificador', palabra, 280]
                        # if identificador not in self.tabla_simbolos:
                        if next((item for item in self.tabla_simbolos if item['lexeme'] == palabra), None) == None:
                            identificador = {
                                'lexeme': palabra,
                                'token': 'identifier',
                                'type': 'int',
                                'value': self.id
                            }
                            self.id += 1
                            self.tabla_simbolos.append(identificador)
                    self.tokens.append(palabra)
                    palabra = ''
                    # i += 1
            # Error
            else:
                if str.isspace(actual) or actual in self.caracteres_simples:
                    estado_actual = 0
                    # print('Error:', palabra)
                    col = i - len(palabra) + 1
                    self.tabla_errores.append([palabra, num_linea, col])
                    print('Error léxico en la línea {}, columna {}: {}.'.format(num_linea, col, palabra))
                    self.tokens.append(palabra)
                    palabra = ''
                else:
                    palabra += actual
                    i += 1

    def siguiente(self):
        if len(self.tokens) < 1:
            return '$'
        return self.tokens.pop(0)

    def imprimir(self):
        DataTable(['Lexeme', 'Token', 'Type', 'Value'], self.tabla_simbolos).print()
        # encabezado = ['Palabras reservadas']
        # ancho_cols = [20]
        # tabla = Table(encabezado, ancho_cols)
        # tabla.print_header()
        # for fila in self.tabla_palabras_reservadas:
        #     tabla.add_row(fila)
        # tabla.print_line()

        # encabezado = ['Tipo', 'Nombre', 'Valor']
        # ancho_cols = [25, 20, 9]
        # tabla = Table(encabezado, ancho_cols)
        # tabla.print_header()
        # for fila in self.tabla_simbolos:
        #     tabla.add_row(fila)
        # tabla.print_line()

        # encabezado = ['Error', 'Línea', 'Columna']
        # ancho_cols = [15, 6, 8]
        # tabla = Table(encabezado, ancho_cols)
        # tabla.print_header()
        # for fila in self.tabla_errores:
        #     tabla.add_row(fila)
        # tabla.print_line()


def main():
    al = AnalizadorLexico()

    path = input('Escribe el nombre del archivo: ')

    with open(path) as programa_fuente:
        num_linea = 1
        for linea in programa_fuente:
            al.analizar(linea, num_linea)
            num_linea += 1
    al.imprimir()


if __name__ == '__main__':
    main()
