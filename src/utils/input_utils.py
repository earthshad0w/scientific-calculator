# input_utils.py

from decimal import Decimal, InvalidOperation
import re
from math import sqrt
import os

def clear_screen():
    # Works for Windows, macOS, and Linux
    os.system('cls' if os.name == 'nt' else 'clear')


def get_decimal_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == "q":
            print("Quitting program...")
            exit()
        try:
            return Decimal(user_input)
        except InvalidOperation:
            print("Invalid input. Please enter a valid number or 'q' to quit.")

def get_integer_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == "q":
            print("Quitting program...")
            exit()
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer or 'q' to quit.")



def get_choice_input(prompt, min_value, max_value):
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == "q":
            print("Quitting program...")
            exit()
        try:
            choice = int(user_input)
            if min_value <= choice <= max_value:
                return choice
            else:
                print(f"Invalid input. Please enter a number between {min_value} and {max_value}, or 'q' to quit.")
        except ValueError:
            print("Invalid input. Please enter a whole number or 'q' to quit.")


def get_letter_choice(prompt):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    while True:
        user_input = input(prompt).strip().lower()

        if user_input == "q":
            print("Quitting program...")
            exit()

        if user_input in alphabet:
            return user_input
        else:
            print("Invalid input. Please enter a single letter (a–z) or 'q' to quit.")



def smart_decimal_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()

        if user_input == "q":
            print("Quitting program...")
            exit()

        try:
            user_input = user_input.replace(' ', '')  # remove spaces

            # Handle expressions like 3*sqrt(2)
            if '*sqrt(' in user_input:
                multiplier_str, sqrt_part = user_input.split('*sqrt(')
                radicand_str = sqrt_part.rstrip(')')
                multiplier = float(multiplier_str)
                radicand = float(radicand_str)
                return Decimal(multiplier * sqrt(radicand))

            # Handle expressions like 2√5
            if '√' in user_input and not user_input.startswith('√'):
                multiplier_str, radicand_str = user_input.split('√')
                multiplier = float(multiplier_str)
                radicand = float(radicand_str)
                return Decimal(multiplier * sqrt(radicand))

            # Handle sqrt(x)
            if user_input.startswith("sqrt(") and user_input.endswith(")"):
                value = float(user_input[5:-1])
                return Decimal(sqrt(value))

            # Handle √x
            if user_input.startswith("√"):
                value = float(user_input[1:])
                return Decimal(sqrt(value))

            # Handle fractions like 3/4
            if '/' in user_input:
                parts = user_input.split('/')
                if len(parts) != 2:
                    raise ValueError("Malformed fraction.")
                numerator, denominator = map(float, parts)
                return Decimal(numerator / denominator)

            # Fallback: try as a regular number
            return Decimal(user_input)

        except (InvalidOperation, ValueError, ZeroDivisionError, IndexError):
            print("Invalid input. Please enter a valid number (e.g., 5.5, 3/4, sqrt(2), √2, 3*sqrt(2)).")












# def get_decimal_input(prompt):
#     while True:
#         user_input = input(prompt)
#         try:
#             return Decimal(user_input)
#         except InvalidOperation:
#             print("Invalid input. Please enter a valid number.")



# def get_choice_input(prompt, min_value, max_value):
#     while True:
#         user_input = input(prompt)
#         try:
#             choice = int(user_input)
#             if min_value <= choice <= max_value:
#                 return choice
#             else:
#                 print(f"Invalid input. Please enter a number between {min_value} and {max_value}.")
#         except ValueError:
#             print("Invalid input. Please enter a whole number.")



# def smart_decimal_input(prompt):
#     while True:
#         user_input = input(prompt).strip().lower()
        
#         if user_input == "q":
#             print("Quitting program...")
#             exit()

#         try:
#             # Handle sqrt(x) or √x
#             if user_input.startswith("sqrt(") and user_input.endswith(")"):
#                 value = float(user_input[5:-1])
#                 return Decimal(sqrt(value))
#             elif user_input.startswith("√"):
#                 value = float(user_input[1:])
#                 return Decimal(sqrt(value))

#             # Handle fractions like 3/4
#             if '/' in user_input:
#                 numerator, denominator = map(float, user_input.split('/'))
#                 return Decimal(numerator / denominator)

#             # Fallback: try regular Decimal
#             return Decimal(user_input)

#         except (InvalidOperation, ValueError, ZeroDivisionError):
#             print("Invalid input. Please enter a valid number (e.g., 5.5, 3/4, sqrt(2), √2).")