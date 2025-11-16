import math
from decimal import Decimal, InvalidOperation
from fractions import Fraction
from src.utils.input_utils import get_decimal_input
from src.utils.input_utils import get_choice_input
from src.utils.input_utils import get_integer_input
from src.geometry import Area_and_Perimeter_Functions as geo_tools


pi = Decimal("3.141592653589793238462643383279")

# Volume of a rectangular prism
def volume_of_a_rectangular_prism(length, width, height):
    return round(length * width * height, 2)

# Volume of a triangular prism
def volume_of_a_triangular_prism(base, height, prism_height):
    face = geo_tools.triangle_area(base, height)
    return round(face * prism_height)

# Volume of a regular polygonal prism
def volume_of_regular_polygonal_prism():
    # Dimensions of polygon
    polygon_number_of_sides = get_integer_input("Enter the number of sides: ")
    while polygon_number_of_sides < 4:
        polygon_number_of_sides = int(input("Number of sides needs to be greater than 4. Enter number of sides: "))
    polygon_side_length = get_decimal_input("Enter the side length: ")
    polygon_apothem_length = get_decimal_input("Enter the apothem length: ")
    solid_height = get_decimal_input("Enter the solid's height: ")

    # Calculating face area
    polygon_face = geo_tools.regular_polygon_area(polygon_number_of_sides,
    polygon_side_length, polygon_apothem_length)

    return round(polygon_face * solid_height, 2)

# Volaume of a cylinder
def volume_of_a_cylinder(radius, height):
    face = geo_tools.circle_area(radius)
    return round(face * height, 2)

# Volume of a regular pyramid: V = (1/3) * B * h
def volume_of_pyramid():
    print("Select the base shape of the pyramid:")
    print("1. Triangle")
    print("2. Rectangle or Square")
    print("3. Regular Polygon")

    base_choice = get_choice_input("Enter your choice (1–3): ", 1, 3)

    if base_choice == 1:  # Triangle base
        print("Choose input method for triangle base:")
        print("1. Use base and height")
        print("2. Use three sides (Heron's formula)")
        triangle_input_method = get_choice_input("Enter 1 or 2: ", 1, 2)

        if triangle_input_method == 1:
            base = get_decimal_input("Enter the base length: ")
            base_height = get_decimal_input("Enter the base height: ")
            base_area = geo_tools.triangle_area(base, base_height)

        elif triangle_input_method == 2:
            side_a = get_decimal_input("Enter the first side: ")
            side_b = get_decimal_input("Enter the second side: ")
            side_c = get_decimal_input("Enter the third side: ")
            s = (side_a + side_b + side_c) / 2
            base_area = (s * (s - side_a) * (s - side_b) * (s - side_c)).sqrt()

        height = get_decimal_input("Enter the height of the pyramid: ")

    elif base_choice == 2:  # Rectangle or square base
        length = get_decimal_input("Enter the length of the rectangle: ")
        width = get_decimal_input("Enter the width of the rectangle: ")
        base_area = length * width
        height = get_decimal_input("Enter the height of the pyramid: ")

    elif base_choice == 3:  # Regular polygon base
        number_of_sides = get_integer_input("Enter the number of sides of the base: ")
        side_length = get_decimal_input("Enter the side length: ")
        apothem = get_decimal_input("Enter the apothem length: ")
        perimeter = geo_tools.regular_polygon_perimeter(number_of_sides, side_length)
        base_area = Decimal("0.5") * perimeter * apothem
        height = get_decimal_input("Enter the height of the pyramid: ")

    volume = (Decimal("1") / Decimal("3")) * base_area * height
    return round(volume, 2)

# Volume of a cone: V = (1/3) * pi * r^2 * h
def volume_of_cone():
    print("Volume of a Cone")
    radius = get_decimal_input("Enter the radius: ")
    height = get_decimal_input("Enter the height: ")
    base_area = geo_tools.circle_area(radius)
    volume = (Decimal("1") / Decimal("3")) * base_area * height
    return round(volume, 2)

# Volume of a sphere: V = (4/3) * pi * r^3
def volume_of_sphere():
    print("Volume of a Sphere")
    radius = get_decimal_input("Enter the radius: ")
    volume = (Decimal("4") / Decimal("3")) * pi * radius ** 3
    return round(volume, 2)


    
