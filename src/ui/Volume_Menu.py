# Volume_Menu.py

from decimal import Decimal
from src.utils.input_utils import smart_decimal_input
from src.utils.input_utils import get_choice_input
from src.geometry import Area_and_Perimeter_Functions as geo_tools
from src.geometry import Volume_Functions


def run_volume_menu():
    print(
        "Press 1 for volume of a rectangular prism.\n"
        "Press 2 for volume of a triangular prism.\n"
        "Press 3 for volume of a regular polygonal prism.\n"
        "Press 4 for volume of a cylinder.\n"
        "Press 5 for volume of a pyramid.\n"
        "Press 6 for volume of a cone.\n"
        "Press 7 for volume of a sphere.\n"
    )

    function_choice = get_choice_input("Enter your choice (1–7): ", 1, 7)
    #function_choice = get_choice_input("Enter your choice: ")
    while not (1 <= function_choice <= 7):
        get_choice_input("Invalid input. Enter your choice: ")
        function_choice = int(input())

    if function_choice == 1:
        length = smart_decimal_input("Enter the length: ")
        width = smart_decimal_input("Enter the width: ")
        height = smart_decimal_input("Enter the height: ")
        volume = Volume_Functions.volume_of_a_rectangular_prism(length, width, height)
        print(f"The volume is {volume} cubic units.")

    elif function_choice == 2:
        base = smart_decimal_input("Enter the base of of the triangle's face: ")
        height = smart_decimal_input("Enter the height of the triangle's face: ")
        prism_height = smart_decimal_input("Enter the height of the prism: ")
        volume = Volume_Functions.volume_of_a_triangular_prism(base, height, prism_height)
        print(f"The volume is {volume} cubic units.")

    elif function_choice == 3:
        volume = Volume_Functions.volume_of_regular_polygonal_prism()
        print(f"The volume is {volume} cubic units.")

    elif function_choice == 4:
        radius = smart_decimal_input("Enter the radius: ")
        height = smart_decimal_input("Enter the height: ")
        volume = Volume_Functions.volume_of_a_cylinder(radius, height)
        print(f"The volume is {volume} cubic units.")

    elif function_choice == 5:
        volume = Volume_Functions.volume_of_pyramid()
        print(f"The volume is {volume} cubic units.")

    elif function_choice == 6:
        volume = Volume_Functions.volume_of_cone()
        print(f"The volume is {volume} cubic units.")

    elif function_choice == 7:
        volume = Volume_Functions.volume_of_sphere()
        print(f"The volume is {volume} cubic units.")


if __name__ == "__main__":
    terminate_program = True

    while terminate_program:
        run_volume_menu()

        print("Press 'y' to continue or 'q' to exit")
        user_quit = input().lower()
        while user_quit not in ["y", "q"]:
            print("Invalid response. Press 'y' to continue or 'q' to exit ")
            user_quit = input().lower()

        if user_quit == "q":
            terminate_program = False
