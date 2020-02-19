class DataTable:

    def __init__(self, headers, dataset):
        self.__headers = headers
        self.__dataset = dataset
        self.__format_string = '|'
        self.__separator = '+'
        self.__create()

    def __create(self):
        column_widths = []
        for header in self.__headers:
            column_widths.append(len(header))

        for index, key in enumerate(self.__dataset[0].keys()):
            for element in self.__dataset:
                if len(str(element[key])) > column_widths[index]:
                    column_widths[index] = len(str(element[key]))
            column_widths[index] += 1

        for width in column_widths:
            self.__separator = self.__separator + '-' * width + '+'
            self.__format_string += '{:<' + str(width) + '}|'

    def print(self):
        print(self.__separator)
        print(self.__format_string.format(*self.__headers))
        print(self.__separator)

        for x in self.__dataset:
            print(self.__format_string.format(*x.values()))
            print(self.__separator)

def main():
    headers = ['Lexeme', 'Token', 'Type', 'Value']
    dataset = [
        { 'lexeme': 'if', 'token': 'keyword',           'type': 'keyword',           'value': 300 },
        { 'lexeme': 'a',  'token': 'identifier',        'type': 'int',               'value': 0   },
        { 'lexeme': ';',  'token': 'special character', 'type': 'special character', 'value': 59  },
    ]

    DataTable(headers, dataset).print()


if __name__ == '__main__':
    main()