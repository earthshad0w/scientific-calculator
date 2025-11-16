# Surface_Area_of_Prisms_and_Cylinders.py (sandbox)
from src.geometry import Surface_Area_Functions_v2 as area_functions
from src.utils.input_utils import get_choice_input



def run_surface_area_menu():
    print(
    "Please choose a function:\n"
    "Press 1 for the lateral area of a prism.\n"
    "Press 2 for the surface area of a prism.\n"
    "Press 3 for the lateral area of a cylinder.\n"
    "Press 4 for the surface area of a cylinder.\n"
    "Press 5 for the lateral area of a pyramid.\n"
    "Press 6 for the surface area of a pyramid.\n"
    "Press 7 for the lateral area of a cone.\n"
    "Press 8 for the surface area of a cone.\n"
    "Press 9 for the surface area of a sphere."
)

    # User input for desired function
    function_choice = get_choice_input("Enter your choice (1–9): ", 1, 9)
    while not (1 <= function_choice <= 9):
        print("Invalid choice. Please choose a number between 1 and 8.")
        function_choice = int(input())

    if function_choice == 1:
        lateral_area = area_functions.lateral_area_of_prism()
        print(f"The lateral area of the prism is {lateral_area} square units.")

    elif function_choice == 2:
        surface_area = area_functions.surface_area_of_prism()
        print(f"The surface area of the prism is {surface_area} square units.")

    elif function_choice == 3:
        lateral_area = area_functions.lateral_area_of_cylinder()
        print(f"The lateral area of the cylinder is {lateral_area} square units.")

    elif function_choice == 4:
        surface_area = area_functions.surface_area_of_cylinder()
        print(f"The surface area of the cylinder is {surface_area} square units.")

    elif function_choice == 5:
        lateral_area = area_functions.lateral_area_of_pyramid()
        print(f"The lateral area of the pyramid is {lateral_area} square units.")

    elif function_choice == 6:
        surface_area = area_functions.surface_area_of_pyramid()
        print(f"The surface area of the pyramid is {surface_area} square units.")

    elif function_choice == 7:
        lateral_area = area_functions.lateral_area_of_cone()
        print(f"The lateral area of the cone is {lateral_area} square units.")

    elif function_choice == 8:
        surface_area = area_functions.surface_area_of_cone()
        print(f"The surface area of the cone is {surface_area} square units.")

    elif function_choice == 9:
        surface_area = area_functions.surface_area_of_sphere()
        print(f"The surface area of the sphere is {surface_area} square units.")
    
    
if __name__ == "__main__":
    terminate_program = True

    while terminate_program:
        run_surface_area_menu()

        print("Press 'y' to continue or 'q' to exit")
        user_quit = input().lower()
        while user_quit not in ["y", "q"]:
            print("Invalid response. Press 'y' to continue or 'q' to exit ")
            user_quit = input().lower()

        if user_quit == "q":
            terminate_program = False





