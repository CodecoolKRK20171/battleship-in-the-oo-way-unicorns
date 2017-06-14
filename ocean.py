class Ocean:

    def __init__(self):
        self.is_hidden = False
        self.coordinates = ()
        self.board = {}

        rows = range(1, 11)
        columns = []

        for row in rows:
            columns.append(row)
            for column in columns:
                coordinates.append((column, row))

    def add_to_ocean(self, coord, item):

        self.board[coord] = item

    def add_water(self):

        for coordinate in self.coordinates:
            if coordinate not in self.board.keys():
                board[coordinate] = Water()
