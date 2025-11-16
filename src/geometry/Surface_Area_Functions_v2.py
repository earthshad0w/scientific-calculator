# Surface_Area_of_Prisms_and_Cylinders_Functions.py

import math
from decimal import Decimal, InvalidOperation
from fractions import Fraction
from src.utils.input_utils import get_decimal_input
from src.utils.input_utils import smart_decimal_input
from src.utils.input_utils import get_choice_input
from src.geometry import Area_and_Perimeter_Functions as geo_tools


# Surface area of a cylinder formula: 2*pi*r*h + 2*pi*r**2

pi = Decimal("3.141592653589793238462643383279")

# Lateral area of a prism: L = P*h
def lateral_area_of_prism():
    print("Select type of polygonal base:\n1. Triangle\n2. Quadrilateral\n3. Any other regular polygon")
    user_choice = get_choice_input("Enter your choice (1–3): ", 1, 3)

    if user_choice == 1:
        # Triangle base
        side_1 = get_decimal_input("Enter the first side: ")
        side_2 = get_decimal_input("Enter the second side: ")
        side_3 = get_decimal_input("Enter the third side: ")
        perimeter = geo_tools.triangle_perimeter(side_1, side_2, side_3)
        solid_height = get_decimal_input("Enter the solid's height: ")
        lateral_area = perimeter * solid_height

    elif user_choice == 2:
        quad_choice = get_choice_input("Press 1 for rectangular base, 2 for parallelogram base: ", 1, 2)

        if quad_choice == 1:
            length = get_decimal_input("Enter the length: ")
            width = get_decimal_input("Enter the width: ")
            perimeter = geo_tools.parallelogram_perimeter(length, width)
            solid_height = get_decimal_input("Enter the solid's height: ")
            lateral_area = perimeter * solid_height

        elif quad_choice == 2:
            base = get_decimal_input("Enter the base length: ")
            side = get_decimal_input("Enter the side length (non-base): ")
            perimeter = geo_tools.parallelogram_perimeter(base, side)
            solid_height = get_decimal_input("Enter the solid's height: ")
            lateral_area = perimeter * solid_height

    elif user_choice == 3:
        num_sides = get_decimal_input("Enter the number of sides: ")
        while num_sides < 4:
            num_sides = get_decimal_input("Must be 4 or more. Enter number of sides: ")
        side_length = get_decimal_input("Enter the side length: ")
        solid_height = get_decimal_input("Enter the solid's height: ")
        perimeter = geo_tools.regular_polygon_perimeter(num_sides, side_length)
        lateral_area = perimeter * solid_height

    return round(lateral_area, 2)

# Surface area of a prism: S = L + 2B
def surface_area_of_prism():
    print("Select type of polygonal base:\n1. Triangle\n2. Quadrilateral\n3. Any other regular polygon")
    user_choice = get_choice_input("Enter your choice (1–3): ", 1, 3)

    if user_choice == 1:
        # Triangle base
        base = get_decimal_input("Enter the base length of the triangle: ")
        height = get_decimal_input("Enter the height of the triangle: ")
        base_area = geo_tools.triangle_area(base, height)

        side_1 = get_decimal_input("Enter the first side: ")
        side_2 = get_decimal_input("Enter the second side: ")
        side_3 = get_decimal_input("Enter the third side: ")
        perimeter = geo_tools.triangle_perimeter(side_1, side_2, side_3)

        solid_height = get_decimal_input("Enter the solid's height: ")
        lateral_area = perimeter * solid_height
        surface_area = lateral_area + (2 * base_area)

    elif user_choice == 2:
        quad_choice = get_choice_input("Press 1 for rectangular base, 2 for parallelogram base: ", 1, 2)

        if quad_choice == 1:
            length = get_decimal_input("Enter the length: ")
            width = get_decimal_input("Enter the width: ")
            solid_height = get_decimal_input("Enter the solid's height: ")

            perimeter = geo_tools.parallelogram_perimeter(length, width)
            base_area = geo_tools.rectangle_area(length, width)
            lateral_area = perimeter * solid_height
            surface_area = lateral_area + (2 * base_area)

        elif quad_choice == 2:
            base = get_decimal_input("Enter the base length: ")
            side = get_decimal_input("Enter the side length (non-base): ")
            height = get_decimal_input("Enter the height of the base: ")
            solid_height = get_decimal_input("Enter the solid's height: ")

            perimeter = geo_tools.parallelogram_perimeter(base, side)
            base_area = geo_tools.parallelogram_area(base, height)
            lateral_area = perimeter * solid_height
            surface_area = lateral_area + (2 * base_area)

    elif user_choice == 3:
        num_sides = get_decimal_input("Enter the number of sides: ")
        while num_sides < 4:
            num_sides = get_decimal_input("Must be 4 or more. Enter number of sides: ")
        side_length = get_decimal_input("Enter the side length: ")
        apothem = get_decimal_input("Enter the apothem: ")
        solid_height = get_decimal_input("Enter the solid's height: ")

        perimeter = geo_tools.regular_polygon_perimeter(num_sides, side_length)
        base_area = Decimal("0.5") * perimeter * apothem
        lateral_area = perimeter * solid_height
        surface_area = lateral_area + (2 * base_area)

    return round(surface_area, 2)
      
# Lateral area of a cylinder: L = 2*pi*r*h
def lateral_area_of_cylinder():
    # Dimensions of cylinder
    cylinder_radius = get_decimal_input("Enter radius of cylinder: ")
    cylinder_height = get_decimal_input("Height of cylinder: ")

    # Calculating lateral area
    lateral_area = geo_tools.circle_circumference(cylinder_radius) * cylinder_height
    
    #Rounding to nearest hundreth
    lateral_area_rounded = round(lateral_area, 2)

    return lateral_area_rounded

# Surface area of a cylinder: 2*pi*r*h + 2*pi*r**2
def surface_area_of_cylinder():
    # Dimensions of cylinder
    cylinder_radius = get_decimal_input("Enter radius of cylinder: ")
    cylinder_height = get_decimal_input("Height of cylinder: ")

    # Calculating lateral area
    lateral_area = geo_tools.circle_circumference(cylinder_radius) * cylinder_height

    # Calculating base area
    base_area = geo_tools.circle_area(cylinder_radius)

    # Calculating surface area
    surface_area = lateral_area + (2 * base_area)

    #Rounding to nearest hundreth
    surface_area_rounded = round(surface_area, 2)

    return surface_area_rounded

# Lateral area of a pyramid: L = (1/2) * P * slant_height
def lateral_area_of_pyramid():
    polygon_number_of_sides = int(input("Enter the number of sides on the base: "))
    while polygon_number_of_sides < 3:
        polygon_number_of_sides = int(input("Number of sides must be 3 or more. Enter again: "))
    
    if polygon_number_of_sides == 3:
        side_a = get_decimal_input("Enter the first side length of the triangle: ")
        side_b = get_decimal_input("Enter the second side length: ")
        side_c = get_decimal_input("Enter the third side length: ")
        slant_height = get_decimal_input("Enter the slant height of the triangle face: ")

        perimeter = geo_tools.triangle_perimeter(side_a, side_b, side_c)
        lateral_area = Decimal("0.5") * perimeter * slant_height

    elif polygon_number_of_sides == 4:
        base_side = get_decimal_input("Enter the side length: ")
        slant_height = get_decimal_input("Enter the slant height: ")

        perimeter = geo_tools.regular_polygon_perimeter(4, base_side)
        lateral_area = Decimal("0.5") * perimeter * slant_height

    else:
        polygon_side_length = get_decimal_input("Enter the side length: ")
        slant_height = get_decimal_input("Enter the slant height: ")

        perimeter = geo_tools.regular_polygon_perimeter(polygon_number_of_sides, polygon_side_length)
        lateral_area = Decimal("0.5") * perimeter * slant_height

    return round(lateral_area, 2)

# Surface area of a pyramid: S = L + B
def surface_area_of_pyramid():
    polygon_number_of_sides = int(input("Enter the number of sides on the base: "))
    while polygon_number_of_sides <= 3:
        polygon_number_of_sides = int(input("Number of sides must be 3 or more. Enter again: "))
    
    if polygon_number_of_sides == 3:
        base_length = get_decimal_input("Enter the base length of the triangle: ")
        base_height = get_decimal_input("Enter the height of the triangular base: ")
        slant_height = get_decimal_input("Enter the slant height of the triangle face: ")

        base_area = geo_tools.triangle_area(base_length, base_height)
        perimeter = geo_tools.triangle_perimeter(base_length, base_length, base_length)  # or allow user to input 3 sides
        lateral_area = Decimal("0.5") * perimeter * slant_height

        surface_area = lateral_area + base_area

    elif polygon_number_of_sides == 4:
        base_side = get_decimal_input("Enter the side length: ")
        base_area = geo_tools.square_area(base_side)
        slant_height = get_decimal_input("Enter the slant height: ")

        perimeter = geo_tools.regular_polygon_perimeter(4, base_side)
        lateral_area = Decimal("0.5") * perimeter * slant_height
        surface_area = lateral_area + base_area


    elif polygon_number_of_sides > 4:
        polygon_side_length = get_decimal_input("Enter the side length: ")
        slant_height = get_decimal_input("Enter the slant height: ")
        apothem = get_decimal_input("Enter the apothem of the base: ")

        perimeter = geo_tools.regular_polygon_perimeter(polygon_number_of_sides, polygon_side_length)
        lateral_area = Decimal("0.5") * perimeter * slant_height
        base_area = geo_tools.regular_polygon_area(polygon_number_of_sides, polygon_side_length, apothem)

        surface_area = lateral_area + base_area

    return round(surface_area, 2)

# Lateral area of a cone: L = π * r * l
def lateral_area_of_cone():
    radius = smart_decimal_input("Enter the radius: ")
    slant_height = smart_decimal_input("Enter the slant height: ")

    lateral_area = pi * radius * slant_height

    return round(lateral_area, 2)

# Surface area of a cone: S = L + B = π * r * l + π * r²
def surface_area_of_cone():
    radius = smart_decimal_input("Enter the radius: ")
    slant_height = smart_decimal_input("Enter the slant height: ")

    lateral_area = pi * radius * slant_height
    base_area = pi * radius ** 2
    surface_area = lateral_area + base_area

    return round(surface_area, 2)

# Surface area of a sphere: A = 4 * pi * r^2
def surface_area_of_sphere():
    print("Surface Area of a Sphere")
    radius = get_decimal_input("Enter the radius: ")
    surface_area = 4 * pi * radius ** 2
    return round(surface_area, 2)

def lateral_area_of_frustum():
    r1 = smart_decimal_input("Enter the radius of the bottom base (r1): ") 
    r2 = smart_decimal_input("Enter the radius of the top base (r2): ")
    l = smart_decimal_input("Enter slant height: ")
    lateral_area = pi * (r1 + r2) * l
    return round(lateral_area, 2)


# [pi * (r1 + r2) * l] + pi * r1^2 + pi * r2^2
def surface_area_of_frustum():
    r1 = smart_decimal_input("Enter the radius of the bottom base (r1): ") 
    r2 = smart_decimal_input("Enter the radius of the top base (r2): ")
    l = smart_decimal_input("Enter slant height: ")
    surface_area = (pi * (r1 + r2) * l) + pi * r1 ** 2 + pi * r2 ** 2
    return round(surface_area, 2)

