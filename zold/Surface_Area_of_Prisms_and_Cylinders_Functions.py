import math
from decimal import Decimal
from fractions import Fraction

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

    # Lateral area of a triangle
    if user_choice == 1:
        print("Enter the first side value:")
        triangle_side_1 = Decimal(input())
        print("Enter the second side value:")
        triangle_side_2 = Decimal(input())
        print("Enter the third side value:")
        triangle_side_3 = Decimal(input())
        triangle_perimeter = triangle_side_1 + triangle_side_2 + triangle_side_3
        print("Enter the solid's height:")
        solid_height = Decimal(input())

        lateral_area = triangle_perimeter * solid_height

    # Lateral area of a quadrilateral
    elif user_choice == 2:
        print("Enter the length:")
        rectangle_length = Decimal(input())
        print("Enter the width:")
        rectangle_width = Decimal(input())
        print("Enter the solid's height:")
        solid_height = Decimal(input())

        lateral_area = (2 * rectangle_length + 2 * rectangle_width) * solid_height 

    # Lateral area of any other regular polygon
    if user_choice == 3:
        print("Enter the number of sides:")
        polygon_number_of_sides = Decimal(input())
        print("Enter the side length:")
        polygon_side_length = Decimal(input())
        print("Enter the solid's height:")
        solid_height = Decimal(input())

        lateral_area = (polygon_side_length * polygon_number_of_sides) * solid_height

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
        print("Enter the base length of the triangular face:")
        triangle_face_base = Decimal(input())
        print("Enter the height of the triangular face:")
        triangle_face_height = Decimal(input())
        base_area_of_face = Decimal("0.5") * triangle_face_base * triangle_face_height
        
        
        #Finding the value of P for triangular prism
        print("Enter the first side value:")
        triangle_side_1 = Decimal(input())
        print("Enter the second side value:")
        triangle_side_2 = Decimal(input())
        print("Enter the third side value:")
        triangle_side_3 = Decimal(input())
        triangle_perimeter = triangle_side_1 + triangle_side_2 + triangle_side_3
        print("Enter the solid's height:")
        solid_height = Decimal(input())

        # Calculate lateral area and storing it to lateral_area
        lateral_area = triangle_perimeter * solid_height
        
        # Calculating surface area of a triangular prism
        surface_area = lateral_area + (2 * base_area_of_face) 

    elif user_choice == 2:
        
        # Dimensions of the quadrilateral
        print("Enter length of the base:")
        quadrilateral_face_length = Decimal(input())
        print("Enter the width of the base:")
        quadrilateral_face_width = Decimal(input())
        print("Enter the solid's height:")
        solid_height = Decimal(input())
                
        # Calculate lateral area and storing it to lateral_area       
        lateral_area = (2 * quadrilateral_face_length + 2 * quadrilateral_face_width) * solid_height 
        
        # Calculating surface area of a rectangular prism
        surface_area = lateral_area + (2 * (quadrilateral_face_length * quadrilateral_face_width)) 
    
    
    elif user_choice == 3:
        # Dimensions of polygon
        polygon_number_of_sides = 0
        print("Enter the number of sides:")
        polygon_number_of_sides = Decimal(input())
        while polygon_number_of_sides < 4:
            print("Number of sides needs to be greater than 4. Enter number of sides:")
            polygon_number_of_sides = Decimal(input())
        print("Enter the side length:")
        polygon_side_length = Decimal(input())
        print("Enter the apothem length")
        polygon_apothem_length = Decimal(input())
        print("Enter the solid's height:")
        solid_height = Decimal(input())

        # Calculating lateral area
        lateral_area = (polygon_side_length * polygon_number_of_sides) * solid_height

        # Calculating face area
        base_area_of_face = (Decimal("0.5") * (polygon_side_length * polygon_number_of_sides) * polygon_apothem_length)

        # Calculating surface area
        surface_area = lateral_area + (2 * base_area_of_face)

    return surface_area
        
# Lateral area of a cylinder: L = 2*pi*r*h

def lateral_area_of_cylinder():
    # Dimensions of cylinder
    lateral_area = 0
    print("Enter radius of cylinder:")
    cylinder_radius = Decimal(input())
    print("Height of cylinder:")
    cylinder_height = Decimal(input())

    # Calculating lateral area
    lateral_area = 2 * pi * cylinder_radius * cylinder_height
    
    #Rounding to nearest hundreth
    lateral_area_rounded = round(lateral_area, 2)

    return lateral_area_rounded

# Surface area of a cylinder: 2*pi*r*h + 2*pi*r**2

def surface_area_of_cylinder():
    # Dimensions of cylinder
    lateral_area = 0
    print("Enter radius of cylinder:")
    cylinder_radius = Decimal(input())
    print("Height of cylinder:")
    cylinder_height = Decimal(input())

    # Calculating lateral area
    lateral_area = 2 * pi * cylinder_radius * cylinder_height

    # Calculating base area
    base_area = 2 * pi * cylinder_radius** 2

    # Calculating surface area
    surface_area = lateral_area + base_area

    #Rounding to nearest hundreth
    surface_area_rounded = round(surface_area, 2)

    return surface_area_rounded
