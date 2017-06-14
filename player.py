from ocean import Ocean
from ship import Ship
class player:

    def __init__(self, name):
        self.name = name
        self.enemy_ocean = Ocean()
        self.player_ocean = Ocean()
        self.init_ships_dict()

    def init_ships_dict(self):
        self.ship_dict = {}
        self.ship_dict['Carrier'] = Ship(5)
        self.ship_dict['Battleship'] = Ship(4)
        self.ship_dict['Cruiser'] = Ship(3)
        self.ship_dict['Submarine'] = Ship(3)
        self.ship_dict['Destroyer'] = Ship(2)

    def add_ship_to_ocean(self, ship_name, coordinates, turn=True):
        if ship_name not in self.ship_dict.keys():
            raise NameError('Invalid ship name')
        ship = self.ship_dict[ship_name]
        ship_lenght = len(ship.squer_list)
        column = coordinates[0]
        row = coordinates[1]
        self.check_range(column, row, ship_lenght, turn)
        self.check_is_water(column, row, ship_lenght, turn)
        for value in range(ship_lenght):
            square = ship.square_list[value]
            if turn is True:
                self.player_ocean.add_to_ocean((column+value, row), square)
            elif turn is False:
                self.player_ocean.add_to_ocean((column, row+value), square)

    def check_is_water(self, column, row, ship_lenght, turn):
        for x in range(-1, 2):
            for y in range(-1, ship_lenght+1):
                if turn is True:
                    if self.player_ocean.board.get((column+y, row+x)) is not None:
                        raise KeyError
                elif turn is False:
                    if self.player_ocean.board.get((column+x, row+y)) is not None:
                        raise KeyError

    def check_range(self, column, row, ship_lenght, turn):
        max_value = 9
        if trun is True:
            if column + ship_lenght > max_value:
                raise KeyError
        if turn is False:
            if row + ship_lenght > max_value:
                raise KeyError
