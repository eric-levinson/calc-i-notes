import sympy

def find_critical_values(function):
  # Find the first derivative of the function
  first_derivative = sympy.diff(function)
  
  # Find the critical values by setting the first derivative equal to 0 and solving for x
  critical_values = sympy.solve(first_derivative)
  
  # Return the critical values
  return critical_values

# Define the function using sympy
x = sympy.Symbol('x')
function = x**3 + 3*x**2

# Find the critical values
critical_values = find_critical_values(function)

# Print the critical values
print(f"Critical values: {critical_values}")
