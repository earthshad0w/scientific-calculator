# Area_and_Perimeter_Functions
import math
from decimal import Decimal


pi = math.pi

# Perimeter of a triangle
def triangle_perimeter(side_1, side_2, side_3):
    return side_1 + side_2 + side_3

# Area of a triangle
def triangle_area(base, height):
    return Decimal("0.5") * base * height

# Perimeter of a quadrilateral
def parallelogram_perimeter(length, height):
    return 2 * (length + height)

# Perimeter of irregular quadrilateral
def irregular_quadrilateral_perimeter(side_1, side_2, side_3, side_4):
    return side_1 + side_2 + side_3 + side_4

# Area of a rectangle
def rectangle_area(length, width):
    return length * width

# Area of a quadrilateral
def parallelogram_area(length, height):
    return length * height

def square_perimeter(side):
    return side * 4

def square_area(side):
    return side ** 2

def trapezoid_area(base_a, base_b, height):
    return Decimal("0.5") * (base_a + base_b) * height

def irregular_quadrilateral_perimeter(a, b, c, d):
    return a + b + c + d

# Perimeter of a regular polygon
def regular_polygon_perimeter(number_of_sides, side_length):
    return number_of_sides * side_length

# Area of a regular polygon
def regular_polygon_area(number_of_sides, side_length, apothem):
    return Decimal("0.5") * number_of_sides * side_length * apothem

def circle_circumference(radius):
    return 2 * pi * radius

def circle_area(radius):
    return pi * radius ** 2

