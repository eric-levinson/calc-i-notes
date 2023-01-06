def f(x):
    return 15

def g(x):
    return -5

import sympy

x = sympy.Symbol('x')

limit = sympy.limit((f(x)/g(x)) - 7, x, -2)
print(f"The limit of [f(x)/g(x) - 7] as x approaches -2 is {limit}.")