import sympy

def evaluate_limit_with_table(f, x_values):
    # Print the table header
    print("x\t\tf(x)")
    print("-------------------------")
    
    # Evaluate the function at each x value and print the results
    for x in x_values:
        print(f"{x}\t\t{f(x)}")

# Define the function f(x)
def f(x):
    # Return the value of f(x) for the given range of x values
    if -x**2 + 4*x - 1 <= x <= x**2 - 4*x + 7:
        return x**2 - 4*x + 7
    else:
        return -x**2 + 4*x - 1

# Test the function with a list of x values
x_values = [x/10 for x in range(-30, 51)]
evaluate_limit_with_table(f, x_values)