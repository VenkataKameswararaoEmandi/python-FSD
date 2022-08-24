
import sympy
x = sympy.Symbol('x')
f = x**2
derivative = f.diff(x)
print(derivative)

import sympy as sym
x = sym.Symbol('x')
function = 2*x ** 4 + 7 * x ** 3
derivitive = sym.diff(function)
print(derivitive)
