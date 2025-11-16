import scipy
import math
import sympy
import numpy
from sympy import *

x, y, z = symbols('x y z')
expr = x + 1
expr = expr.subs(x, 2)

a = (x + 2)*2
b = x + x + x + x + x
expr_simplified = simplify(a / b)
expr_simplified = expr_simplified.subs(x, 2)

print(expr_simplified)


