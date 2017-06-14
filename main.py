from ship import Ship
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
    """

    user_ship_type = input("\nEnter a ship type: ").title()

    match = 0
    for ship_type in ship_types:
        if user_ship_type == ship_type:
            ship_types.remove(ship_type)
            match += 1

    if match == 0:
        raise NameError

    return user_ship_type, ship_types

def define_ship_coordinates():
    """
    Gets coordinates from a user.
    Returns:
    -------
    coordinates: tuple
    """
    user_row_number = int(input("Enter a row number: "))
    user_column_number = int(input("Enter a column number: "))
    coordinates_range = range(1,11)

    if (user_row_number and user_column_number) not in coordinates_range:
        raise ValueError

    coordinates = (user_row_number, user_column_number)

    return coordinates

def define_ship_turn():
    """Gets a turn of a placement of ship from a user.
    Returns:
    -------
    user_turn: bool
    """
    user_turn = input("Do you want to place the ship horizontally (put 'h')" +
                      " or vertically? (put 'v') ").lower()

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
    user_ship_type, ship_types = define_ship_type(ship_types)
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
    for ship_type in ship_types:
        print(ship_type)

def main():
    """
    Handles game.
    """
    RED = '\033[91m'
    WHITE = '\033[0m'
    show_screen("hello_screen.csv")
    show_screen("instruction_screen.csv")

    ship_types = ["Carrier", "Battleship", "Cruiser",
                  "Submarine", "Destroyer"]

    while ship_types:
        try:
            user_ship_type, coordinates, user_turn = define_ship_placement(ship_types)
        except NameError:
            print(RED + "\nWrong input mate!" + WHITE)
        except ValueError:
            print(RED + "\nCoordinates should be in a range from 1 to 10." + WHITE)
        #TUTAJ TWORZENIE OBIEKTU STATECZKU




if __name__ == "__main__":
    main()
