from player import Player
import csv

def show_screen(filename):
    """
    Prints screen from a csv file.
    Parameters:
    ----------
    filename: str
    """

    with open(filename, "r") as hello_screen_file:
        hello_screen_reader = csv.reader(hello_screen_file)

        for line in hello_screen_reader:
            print(*line)


def define_ship_type(ship_types):
    """
    Get ship type from a user and returns it.
    Parameters:
    ----------
    ship_types: list

    Returns:
    -------
    user_ship_type: str
    ship_types: list of str

    Raises:
    ------
    NameError: when user's input isn't name of ship type from ship_types list
    """

    user_ship_type = input("\nEnter a ship type: ").title()

    match = 0
    if user_ship_type not in ship_types:
        raise NameError

    return user_ship_type


def define_ship_coordinates():
    """
    Gets coordinates from a user.
    Returns:
    -------
    coordinates: tuple

    Raises:
    ------
    ValueError: when user's input isn't in range from 1 to 10
    """
    user_row_number = int(input("Enter a row number: "))
    user_column_number = int(input("Enter a column number: "))
    coordinates_range = range(10)

    if (user_row_number and user_column_number) not in coordinates_range:
        raise ValueError

    coordinates = (user_column_number, user_row_number)

    return coordinates


def define_ship_turn():
    """Gets a turn of a placement of ship from a user.
    Returns:
    -------
    user_turn: bool

    Raises:
    ------
    NameError: when user's input isn't "y" or "v"
    """
    user_turn = input("Do you want to place the ship horizontally (put 'h')" +
                      " or vertically? (put 'v') ").lower()
    print()

    if user_turn == "h":
        user_turn = True
    elif user_turn == "v":
        user_turn = False
    else:
        raise NameError

    return user_turn


def define_ship_placement(ship_types):
    """
    Gets all information about ship placement.
    Returns:
    -------
    user_ship_type: str
    coordinates: tuple
    user_turn: bool
    """

    show_ship_types(ship_types)
    user_ship_type = define_ship_type(ship_types)
    coordinates = define_ship_coordinates()
    user_turn = define_ship_turn()

    return user_ship_type, coordinates, user_turn


def show_ship_types(ship_types):
    """
    Prints ship types from a ship_types list.
    Parameters:
    ----------
    ship_types: list of str
    """
    print("\nYou can create one of each type of ships: ")
    for key, value in ship_types.items():
        print("{}: {}".format(key, value))

def create_player():
    name = input("Enter your name: ")
    return Player(name)

def place_ships_on_board(player):

    RED = '\033[91m'
    WHITE = '\033[0m'

    ship_types = {"Carrier": "five-masted", "Battleship": "four-masted", "Cruiser": "three-masted",
                  "Submarine": "three-masted", "Destroyer": "two-masted"}

    #ship_types = {"Carrier": "five-masted"}
    while ship_types:
        print(player.player_ocean)
        try:
            user_ship_type, coordinates, user_turn = define_ship_placement(ship_types)
            player.add_ship_to_ocean(user_ship_type, coordinates, user_turn)

        except NameError:
            print(RED + "\nWrong input mate!\n" + WHITE)
        except ValueError:
            print(RED + "\nCoordinates should be in a range from 1 to 10.\n" + WHITE)
        except KeyError:
            print(RED + "\nYou can't place ship next to another or out of edge!\n"+ WHITE)
        else:
            del ship_types[user_ship_type]


def main():
    """
    Handles game.
    """

    show_screen("hello_screen.csv")
    show_screen("instruction_screen.csv")
    player1 = create_player()
    place_ships_on_board(player1)
    player2 = create_player()
    place_ships_on_board(player2)




if __name__ == "__main__":
    main()
