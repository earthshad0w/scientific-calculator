# Geometry app main menu
from src.ui import Area_and_Perimeter_Menu_v2 as area_and_perimeter_menu
from src.ui import Surface_Area_Menu_v2 as surface_area_menu
from src.ui import Volume_Menu as volume_menu
from src.ui import Trigonometry_Menu as trig_menu
from src.utils.input_utils import get_choice_input

def run_geometry_main_menu():

    print("Main menu: \n"
    "Press 1 for area and perimeter.\n"      
    "Press 2 for lateral and surface area.\n"
    "Press 3 for volume.\n"
    "Press 4 for trigonometric functions."
    
    )
    

    function_choice = get_choice_input("Enter your choice (1–4): ", 1, 4)
    while not (1 <= function_choice <= 9):
        print("Invalid choice. Please choose a number between 1 and 4.")
        function_choice = get_choice_input("Enter your choice (1–4): ", 1, 4)

    if function_choice == 1:
        area_and_perimeter_menu.run_area_and_perimeter_menu()

    elif function_choice == 2:
        surface_area_menu.run_surface_area_menu()

    elif function_choice == 3:
        volume_menu.run_volume_menu()
    
    elif function_choice == 4:
        trig_menu.run_trigonometry_menu()



if __name__ == "__main__":
    terminate_program = True

    while terminate_program:
        run_geometry_main_menu()

        print("Press 'y' to continue or 'q' to exit")
        user_quit = input().lower()
        while user_quit not in ["y", "q"]:
            print("Invalid response. Press 'y' to continue or 'q' to exit ")
            user_quit = input().lower()

        if user_quit == "q":
            terminate_program = False