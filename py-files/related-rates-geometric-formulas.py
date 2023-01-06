import math

def solve_related_rates(formula, variables, values):
  # Substitute the given values into the formula
  for variable, value in zip(variables, values):
    formula = formula.replace(variable, str(value))
  
  # Evaluate the resulting expression and return the result
  return eval(formula)

formula = "8 * s"
variables = ["s"]
values = [10]

result = solve_related_rates(formula, variables, values)
print(f"dA/dt = {result}cm^2/sec")

#this solved it dA/dt = 80cm^2/sec
# promt below
#Update this code to solve the following problem using related rates problems using geometric formulas.
#
#All sides of a square are increasing at a rate of 4 centimeters per second.
#
#How fast is the area changing when each side is 10 centimeters?
#
#(Change the output to dA/dt={solution}cm^2/sec)