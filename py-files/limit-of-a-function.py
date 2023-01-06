import sympy

x = sympy.Symbol('x')

def f(x):
    if sympy.ask(sympy.Le(x, -1)):
        return 9 - x**2
    else:
        return 3*x**2 + 2

# Evaluate the limit as x approaches -1 from the left (x -> -1^-)
left_limit = sympy.limit(f(x), x, -1, dir='-')
print(f"The limit as x approaches -1 from the left is {left_limit}.")

# Evaluate the limit as x approaches -1 from the right (x -> -1^+)
right_limit = sympy.limit(f(x), x, -1, dir='+')
print(f"The limit as x approaches -1 from the right is {right_limit}.")