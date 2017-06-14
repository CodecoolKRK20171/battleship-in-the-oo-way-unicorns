class Ocean:

    def __init__(self):
        self.is_hidden = False
        self.coordinates = []
        self.board = {}

        rows = range(1, 11)
        self.columns = []

        for row in rows:
            self.columns.append(row)
            for column in self.columns:
                self.coordinates.append((column, row))
                if (row, column) not in self.coordinates:
                    self.coordinates.append((row, column))

    def add_to_ocean(self, coord, item):

        self.board[coord] = item

    def add_water(self):

        for coordinate in self.coordinates:
            if coordinate not in list(self.board.keys()):
                self.board[coordinate] = Water()

x = Ocean()
