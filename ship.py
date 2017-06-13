class Ship:

    def __init__(self, length):
        self.length = length
        self.is_sunk = False
        self.is_hidden = False
        self.ship = []

        for i in range(length):
            square_i = Square()
            self.ship.append(square_i)

    def mark_square(self, index):
        self.ship[index].mark()

    def mark_is_sunk(self):

        for square in self.ship:
            if not square.is_marked:
                return 
        self.is_sunk = True
