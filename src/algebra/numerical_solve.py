# Numerical solve: Solve equations with one variable.

from sympy import symbols, Eq, solve
import re

def insert_multiplication_symbols(expr):
    # Inserts * between number and variable (e.g., 2x → 2*x, 5(x+1) → 5*(x+1))
    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)
    expr = re.sub(r'(\d)(\()', r'\1*(', expr)
    expr = re.sub(r'([a-zA-Z])(\()', r'\1*(', expr)
    return expr

def solve_for_x(equation_str):
    x = symbols('x')
    left_side, right_side = equation_str.split('=')

    left_side = insert_multiplication_symbols(left_side.strip())
    right_side = insert_multiplication_symbols(right_side.strip())

    equation = Eq(eval(left_side), eval(right_side))
    solution = solve(equation, x)

    return solution[0] if solution else None

# Example test

if __name__ == "__main__":
    
    print(solve_for_x("x(2+2) + 4 = 12"))  # Should print 5.5
