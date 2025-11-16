# Area_and_Perimeter_Menu.py
from src.geometry import Area_and_Perimeter_Functions as geo_tools
from src.utils.input_utils import get_decimal_input


terminate_program = True

while terminate_program == True:

    # Calculate prism lateral surface area
    print(
    "Press 1 for perimeter of a regular quadrilateral.\n"
    "Press 2 for perimeter of an irregular quadrilateral or trapezoid.\n"
    "Press 3 for area of a rectangle or square.\n"
    "Press 4 for area of a regular quadrilateral.\n"
    "Press 5 for area of a trapezoid.\n"
    "Press 6 for perimeter of a triangle.\n"
    "Press 7 for area of a triangle.\n"
    "Press 8 for perimeter of a regular polygon.\n"
    "Press 9 for area of a regular polygon.\n"
    "Press 10 for circumference of a circle.\n"
    "Press 11 for area of a circle."    
    )

    # User input for desired function
    function_choice = int(input())
    while not (1 <= function_choice <= 11):
        print("Invalid choice. Please choose a number between 1 and 11.")
        function_choice = int(input())
    
    # Perimeter of a regular quadrilateral
    if function_choice == 1:
        quadrilateral_length = get_decimal_input("Enter length:")
        quadrilateral_width = get_decimal_input("Enter width:")
        quadrilateral_perimeter = geo_tools.quadrilateral_perimeter(quadrilateral_length, quadrilateral_width)
        print(f"The perimeter is {quadrilateral_perimeter} units.")

    # Perimeter of an irregular quadrilateral or trapezoid
    elif function_choice == 2:
        side_a = get_decimal_input("Enter the length of the first side:")
        side_b = get_decimal_input("Enter the length of the second side:")
        side_c = get_decimal_input("Enter the length of the third side:")
        side_d = get_decimal_input("Enter the length of the fourth side:")
        perimeter = geo_tools.irregular_quadrilateral_perimeter(
            side_a, side_b, side_c, side_d
        )
        print(f"The perimeter is {perimeter} units.")

    # Area of a rectangle or square
    elif function_choice == 3:
        quadrilateral_length = get_decimal_input("Enter length:")
        quadrilateral_width = get_decimal_input("Enter width:")
        quadrilateral_area = geo_tools.quadrilateral_area(quadrilateral_length, quadrilateral_width)
        print(f"The area is {quadrilateral_area} square units.")

    # Area of a regular quadrilateral
    elif function_choice == 4:
        side_length = get_decimal_input("Enter the side length:")
        area = geo_tools.regular_quadrilateral_area(side_length)
        print(f"The area is {area} square units.")

    # Area of a trapezoid
    elif function_choice == 5:
        base1 = get_decimal_input("Enter the length of the first base:")
        base2 = get_decimal_input("Enter the length of the second base:")
        height = get_decimal_input("Enter the height:")
        area = geo_tools.trapezoid_area(base1, base2, height)
        print(f"The area is {area} square units.")

    # Perimeter of a triangle
    elif function_choice == 6:
        side_a = get_decimal_input("Enter the length of the first side:")
        side_b = get_decimal_input("Enter the length of the second side:")
        side_c = get_decimal_input("Enter the length of the third side:")
        perimeter = geo_tools.triangle_perimeter(side_a, side_b, side_c)
        print(f"The perimeter is {perimeter} units.")

    # Area of a triangle
    elif function_choice == 7:
        base = get_decimal_input("Enter the base length:")
        height = get_decimal_input("Enter the height:")
        area = geo_tools.triangle_area(base, height)
        print(f"The area is {area} square units.")

    # Perimeter of a regular polygon
    elif function_choice == 8:
        side_length = get_decimal_input("Enter the side length:")
        num_sides = int(get_decimal_input("Enter the number of sides:"))
        perimeter = geo_tools.regular_polygon_perimeter(side_length, num_sides)
        print(f"The perimeter is {perimeter} units.")

    # Area of a regular polygon
    elif function_choice == 9:
        side_length = get_decimal_input("Enter the side length:")
        num_sides = int(get_decimal_input("Enter the number of sides:"))
        area = geo_tools.regular_polygon_area(side_length, num_sides)
        print(f"The area is {area} square units.")

    # Circumference of a circle
    elif function_choice == 10:
        radius = get_decimal_input("Enter the radius:")
        circumference = geo_tools.circle_circumference(radius)
        print(f"The circumference is {circumference} units.")

    # Area of a circle
    elif function_choice == 11:
        radius = get_decimal_input("Enter the radius:")
        area = geo_tools.circle_area(radius)
        print(f"The area is {area} square units.")
    
    print("Press 'y' to continue or 'q' to exit")
    # user_quit = ""
    user_quit = input()
    user_quit = user_quit.lower()
    while user_quit != "y" and user_quit != "q":
        print("Invalid response. Press 'y' to continue or 'q' to exit ")
        user_quit = input()
        user_quit = user_quit.lower()

    if user_quit == "q":
        terminate_program = False
    
    else:
        terminate_program = True

    

    


