# Surface_Area_of_Prisms_and_Cylinders_Functions.py

import math
from decimal import Decimal, InvalidOperation
from fractions import Fraction
from src.utils.input_utils import get_decimal_input
from src.geometry import Area_and_Perimeter_Functions as geo_tools


# Surface area of a cylinder formula: 2*pi*r*h + 2*pi*r**2

pi = Decimal("3.141592653589793238462643383279")

# Lateral area of a prism: L = P*h
def lateral_area_of_prism():
    lateral_area = 0
    print("Select type of polygonal base:\n1. Triangle\n2. Quadrilateral \n3. Any other regular polygon")
    user_choice = int(input())
    while not (1 <= user_choice < 4):
        print("Invalid choice. Select type of polygonal base:\n1. Triangle\n2. Quadrilateral\n3. Any other regular polygon")
        user_choice = int(input())  # Add this inside the loop

    # Lateral area of a triangular prism
    if user_choice == 1:
        triangle_side_1 = get_decimal_input("Enter the first side value: ")
        triangle_side_2 = get_decimal_input("Enter the second side value: ")
        triangle_side_3 = get_decimal_input("Enter the third side value: ")
        triangle_perimeter = geo_tools.triangle_perimeter(triangle_side_1, triangle_side_2, triangle_side_3)
        solid_height = get_decimal_input("Enter the solid's height: ")

        lateral_area = triangle_perimeter * solid_height

    # Lateral area of a rectangular prism
    elif user_choice == 2:
        rectangle_length = get_decimal_input("Enter the length: ")
        rectangle_width = get_decimal_input("Enter the width: ")
        solid_height = get_decimal_input("Enter the solid's height: ")

        lateral_area = geo_tools.quadrilateral_perimeter(rectangle_length, rectangle_width) * solid_height
        

    # Lateral area of any other regular polygonal prism
    if user_choice == 3:
        polygon_number_of_sides = int(input("Enter the number of sides: "))
        polygon_side_length = get_decimal_input("Enter the side length: ")
        solid_height = get_decimal_input("Enter the solid's height: ")

        lateral_area = geo_tools.regular_polygon_perimeter(polygon_number_of_sides, polygon_side_length) * solid_height

    return lateral_area

# Surface area of a prism: S = L + 2B
def surface_area_of_prism():

    surface_area = 0
    print("Select type of polygonal base:\n1. Triangle\n2. Quadrilateral \n3. Any other regular polygon")
    user_choice = int(input())
    while not (1 <= user_choice <=4):
        print("Invalid choice. Select type of polygonal base:\n1. Triangle\n2. Quadrilateral\n3. Any other regular polygon")
        user_choice = int(input())  # Add this inside the loop
   
    if user_choice == 1:
        
        # Finding the value of B for triangular prism
        triangle_face_base = get_decimal_input("Enter the base length of the triangular face: ")
        triangle_face_height = get_decimal_input("Enter the height of the triangular face: ")
        base_area_of_face = geo_tools.triangle_area(triangle_face_base, triangle_face_height)
        

        #Finding the value of P for triangular prism
        triangle_side_1 = get_decimal_input("Enter the first side value: ")
        triangle_side_2 = get_decimal_input("Enter the second side value: ")
        triangle_side_3 = get_decimal_input("Enter the third side value: ")
        triangle_perimeter = geo_tools.triangle_perimeter(triangle_side_1, triangle_side_2, triangle_side_3)
        solid_height = get_decimal_input("Enter the solid's height: ")

        # Calculate lateral area and storing it to lateral_area
        lateral_area = triangle_perimeter * solid_height
        
        # Calculating surface area of a triangular prism
        surface_area = lateral_area + (2 * base_area_of_face) 

    elif user_choice == 2:
        
        # Dimensions of rectangle
        quadrilateral_face_length = get_decimal_input("Enter length of the base: ")
        quadrilateral_face_width = get_decimal_input("Enter the width of the base: ")
        solid_height = get_decimal_input("Enter the solid's height: ")
                
        # Calculate lateral area and storing it to lateral_area       
        lateral_area = geo_tools.quadrilateral_perimeter(quadrilateral_face_length, quadrilateral_face_width) * solid_height 
        
        # Calculating surface area of a rectangular prism
        surface_area = lateral_area + (2 * geo_tools.quadrilateral_area(quadrilateral_face_length, quadrilateral_face_width))

    
    
    elif user_choice == 3:
        # Dimensions of polygon
        polygon_number_of_sides = int(input("Enter the number of sides: "))
        while polygon_number_of_sides < 4:
            polygon_number_of_sides = int(input("Number of sides needs to be greater than 4. Enter number of sides: "))
        polygon_side_length = get_decimal_input("Enter the side length: ")
        polygon_apothem_length = get_decimal_input("Enter the apothem length: ")
        solid_height = get_decimal_input("Enter the solid's height: ")

        # Reuse perimeter value for both lateral and base area
        polygon_perimeter = geo_tools.regular_polygon_perimeter(polygon_number_of_sides, polygon_side_length)

        # Calculating lateral area
        lateral_area = polygon_perimeter * solid_height

        # Calculating face area
        base_area_of_face = Decimal("0.5") * polygon_perimeter * polygon_apothem_length

        # Calculating surface area
        surface_area = lateral_area + (2 * base_area_of_face)


    return surface_area
        
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
    polygon_side_length = get_decimal_input("Enter the side length: ")
    slant_height = get_decimal_input("Enter the slant height: ")

    perimeter = geo_tools.regular_polygon_perimeter(polygon_number_of_sides, polygon_side_length)
    lateral_area = Decimal("0.5") * perimeter * slant_height

    return round(lateral_area, 2)

# Surface area of a pyramid: S = L + B
def surface_area_of_pyramid():
    polygon_number_of_sides = int(input("Enter the number of sides on the base: "))
    while polygon_number_of_sides < 3:
        polygon_number_of_sides = int(input("Number of sides must be 3 or more. Enter again: "))
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
    radius = get_decimal_input("Enter the radius: ")
    slant_height = get_decimal_input("Enter the slant height: ")

    lateral_area = pi * radius * slant_height

    return round(lateral_area, 2)

# Surface area of a cone: S = L + B = π * r * l + π * r²
def surface_area_of_cone():
    radius = get_decimal_input("Enter the radius: ")
    slant_height = get_decimal_input("Enter the slant height: ")

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


