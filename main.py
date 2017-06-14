from ship import Ship
import csv
def show_screen(filename):

    with open(filename, "r") as hello_screen_file:
        hello_screen_reader = csv.reader(hello_screen_file)

        for line in hello_screen_reader:
            print(*line)

def main():

    show_screen("hello_screen.csv")
    show_screen("instruction_screen.csv")





if __name__ == "__main__":
    main()
