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

        if type(coord) == tuple:
            if coord[0] and coord[1] in range(10):
                self.board[coord] = item
            else:
                raise ValueError("Coordinates do not fit on the board (10x10).")
        else:
            raise TypeError("Invalid coordinate type (expected tuple).")

    def add_water(self):

        for coordinate in self.coordinates:
            if coordinate not in list(self.board.keys()):
                self.board[coordinate] = Water()
