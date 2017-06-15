from water import Water

class Ocean:

    def __init__(self):
        self.is_hidden = False
        self.coordinates = []
        self.board = {}

        rows = range(10)
        self.columns = []

        for row in rows:
            self.columns.append(row)
            for column in self.columns:
                self.coordinates.append((column, row))
                if (row, column) not in self.coordinates:
                    self.coordinates.append((row, column))

    def add_to_ocean(self, coord, item):

        coord_range = range(0, 10)

        if type(coord) == tuple:
            if (coord[0] and coord[1]) in coord_range:
                self.board[coord] = item

        else:
            raise TypeError("Invalid coordinate type (expected tuple).")


    def add_water(self):
        for coordinate in self.coordinates:
            if coordinate not in list(self.board.keys()):
                self.board[coordinate] = Water()


    def get_item_from_ocean(self, coordinates):
        item = self.board[coordinates]
        return item



    def __str__(self):
        return_string = ' |0|1|2|3|4|5|6|7|8|9\n'
        for y in range(0, 10):
            line = '{}|'.format(y)
            for x in range(0, 10):
                if self.board.get((x, y)) is not None: #and not self.is_hidden:
                    board_element = self.board[(x, y)]
                elif self.board.get((x, y)) is None:
                    board_element = ' '
                line += '{}|'.format(board_element)
            line += '\n'
            return_string += line
        return return_string
