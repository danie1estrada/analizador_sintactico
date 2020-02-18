class Table(object):
  """Format text as a table in the command line.
  """

  def __init__(self, header_data, col_width):
    """Creates a new Table object setting up the table header and width for
    each column.
    
    Args:
    header_data: The array that contains the names for each column heading.
    col_width: Integer array with the width (in characters) for each column.
    """
    self.__header_data = header_data
    self.__col_width = col_width
    self.__format_string = "|"
    self.__line = "+"

    self.__create()
    
  def __create(self):
    for width in self.__col_width:
      self.__format_string += "{:<" + str(width) + "}|"
      self.__line = self.__line + "-" * width + "+"

  def print_line(self):
    print(self.__line)

  def print_header(self):
    '''
    Print to the console the table's first row (the header).
    '''
    self.print_line()
    print(self.__format_string.format(*self.__header_data))
    self.print_line()

  def add_row(self, data):
    print(self.__format_string.format(*data))