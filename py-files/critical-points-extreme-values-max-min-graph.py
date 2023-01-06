#critical point and extreme values (max/min) of a function
#!!!!!you need to update f(x) and function!!!!!!
import numpy as np
import matplotlib.pyplot as plt
import sympy

def f(x):
  return x**2/(x+1)

x = np.linspace(-2, 2, 100)

# Get y values from the function
y = f(x)

# Plot the function with a grid
plt.grid(True)
plt.plot(x, f(x))
plt.show()

# Generate x values from -5 to 5 in increments of 0.1
x = np.arange(-5, 5, 1)

# Print the x, y coordinates of the points on the graph
for x_val, y_val in zip(x, y):
  print(f"x: {x_val}, y: {y_val}")


def find_critical_values(function):
  # Find the first derivative of the function
  first_derivative = sympy.diff(function)
  
  # Find the critical values by setting the first derivative equal to 0 and solving for x
  critical_values = sympy.solve(first_derivative)
  
  # Return the critical values
  return critical_values

# Define the function using sympy
x = sympy.Symbol('x')
function = x**2/(x+1)

# Find the critical values
critical_values = find_critical_values(function)

# Print the critical values
print(f"Critical values: {critical_values}")

