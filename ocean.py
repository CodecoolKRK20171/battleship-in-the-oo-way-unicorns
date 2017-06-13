class Ocean:

    def __init__(self, ship_coords):
        self.ship_coords = ship_coords
        self.is_hidden = False
        self.coordinates = ()

        rows = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        for row in rows:
            columns.append(row)
            for column in columns:
                coordinates.append((column, row))
