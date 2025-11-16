# Basic Trigonometry functions
import math
import numpy as np

# Pythagorean theorem solve for missing leg measure.
def solve_leg(side_b, side_c):
    return round(math.sqrt(side_c**2 - side_b**2), 2)

# Pythagorean theorem solve for hypotenuse.
def solve_hypotenuse(side_a, side_b):
    return round(math.sqrt(side_a**2 + side_b**2))

# Find sin ratio.
def find_sin_ratio(opposite_leg, hypotenuse):
    return round(opposite_leg/hypotenuse, 4)

# Find cos ratio. 
def find_cos_ratio(adjacent_leg, hypotenuse):
    return round(adjacent_leg/hypotenuse, 4)

# Find tan ratio.
def find_tan_ratio(opposite_leg, adjacent_leg):
    return round(opposite_leg/adjacent_leg, 4)

# Find acute angle measure of right triangle.
def find_angle_from_sin(sin_ratio):
    if 0 <= sin_ratio <= 1:
        angle = math.degrees(math.asin(sin_ratio))
        return round(angle, 1)

def find_angle_from_cos(cos_ratio):
    if 0 <= cos_ratio <= 1:
        angle = math.degrees(math.acos(cos_ratio))
        return round(angle, 1)

def find_angle_from_tan(tan_ratio):
    # Tan has a domain of all real numbers
    angle = math.degrees(math.atan(tan_ratio))
    return round(angle, 1)

# DOUBLE CHECK GPT
def find_missing_side_from_sin(angle_deg, side, keyword):
    angle_rad = np.radians(float(angle_deg))
    side = float(side)

    if keyword == "opposite leg":
        return round(np.sin(angle_rad) * side, 2)  # side = hypotenuse
    elif keyword == "hypotenuse":
        return round(side / np.sin(angle_rad), 2)  # side = opposite
    else:
        raise ValueError("Keyword must be 'opposite leg' or 'hypotenuse'")

# DOUBLE CHECK GPT
def find_missing_side_from_cos(angle_deg, side, keyword):
    angle_rad = np.radians(float(angle_deg))
    side = float(side)

    if keyword == "adjacent leg":
        return round(np.cos(angle_rad) * side, 2)  # side = hypotenuse
    elif keyword == "hypotenuse":
        return round(side / np.cos(angle_rad), 2)  # side = adjacent
    else:
        raise ValueError("Keyword must be 'adjacent leg' or 'hypotenuse'")

def find_missing_side_from_tan(angle_deg, side, keyword):
    angle_rad = np.radians(float(angle_deg)) 
    side = float(side)
    if keyword == "adjacent leg":
        return round(side / np.tan(float(angle_rad)), 2)
    elif keyword == "opposite leg":
        return round(np.tan(float(angle_rad)) * side, 2)


# def find_missing_side_from_tan(angle_deg, side, keyword):
#     angle_rad = np.radians(float(angle_deg)) 
    
#     if keyword == "adjacent leg":
#         return side / np.tan(angle_rad)
#     elif keyword == "opposite leg":
#         return np.tan(angle_rad) * side
#     else:
#         raise ValueError("Keyword must be 'adjacent leg' or 'opposite leg'")

# def find_missing_side_from_tan(angle_deg, known_side, solve_for="adjacent"):
#     angle_rad = np.radians(angle_deg)
#     if solve_for == "adjacent":
#         return known_side / np.tan(angle_rad)
#     elif solve_for == "opposite":
#         return known_side * np.tan(angle_rad)
#     else:
#         raise ValueError("solve_for must be 'adjacent' or 'opposite'")


'''Solve for distance between coordinates. Not sure where this should go yet.
Will determine later'''

# def distance_formula(x1, y1, x2, y2):
#     return sqrt((x2-x1)**2 + (y2-y1)**2)

