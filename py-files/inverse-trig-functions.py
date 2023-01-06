import sympy as sp

# Define the function using sympy symbols
x = sp.Symbol('x')
f = (4*x**3 + 1) * sp.asin(x**3)

# Use the product rule to compute the derivative
g = 4*x**3 + 1
h = sp.asin(x**3)
derivative = g * sp.diff(h, x) + h * sp.diff(g, x)

# Evaluate each derivative and use the chain rule
g_derivative = 12*x**2
h_derivative = x**3 / sp.sqrt(1 - x**6)
derivative = g_derivative * h_derivative + h * g_derivative

# Print the derivative in the desired format
print(f"f'(x) = {derivative}")
#we did not pass this section :(