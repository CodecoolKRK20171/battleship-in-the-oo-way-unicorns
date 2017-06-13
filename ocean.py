class Ocean:

    def __init__(self, ship_coords):
        self.ship_coords = ship_coords
        self.is_hidden = False
        self.coordinates = ()

        rows = range(1, 11)
        columns = []

        for row in rows:
            columns.append(row)
            for column in columns:
                coordinates.append((column, row))
