import math

def evaluate_limit_with_table(f, x_values):
    # Print the table header
    print("x\t\tf(x)")
    print("-------------------------")
    
    # Evaluate the function at each x value and print the results
    for x in x_values:
        if x**2-7*x+12 == 0:
            print(f"{x}\t\tundefined")
        else:
            print(f"{x}\t\t{f(x)}")

# Test the function with the function f(x) = (x^2 - 4)/(x^2 + 5x + 6)
#x_values = [0.9, 0.99, 0.999, 1.001, 1.01, 1.1]
# Array incrementing by 0.1 from 3 to 5
x_values = [x/10 for x in range(30, 51)]
evaluate_limit_with_table(lambda x: (1/x-1/5)/(x-5), x_values)
