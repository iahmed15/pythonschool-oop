from wheat_class import *
from potato_class import *


def display_crop_menu():
    """Shows the crop types that can be generated to the user"""
    
    print()
    print("Which crop would you like to create?")
    print()
    print("1. Potato")
    print("2. Wheat")
    print()
    print("Please select an option from the above menu")


def select_option():
    """Provides the user with the interface to input the crop type they want
    to create and instantiate to then grow

    Returns:
        choice (int): the crop type the user wants to create"""
    valid_option = False
    while not valid_option:
        try:
            choice = int(input("Option selected: "))
            if choice in (1, 2):
                valid_option = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")

    return choice


def create_crop():
    """Allows the user to choose which crop type they want to create and
    instantiate to then grow

    Returns:
        new_crop (object): the instantiated class object"""
    display_crop_menu()
    choice = select_option()
    if choice == 1:
        new_crop = Potato()
    elif choice == 2:
        new_crop = Wheat()

    return new_crop


def main():
    new_crop = create_crop()
    manage_crop(new_crop)


if __name__ == "__main__":
    main()
