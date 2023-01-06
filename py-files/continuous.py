import math

def evaluate_limit_with_table(f, x_values, a):
    # Print the table header
    print("x\t\tf(x)")
    print("-------------------------")
    
    # Evaluate the function at each x value and print the results
    for x in x_values:
        if x == a:
            # Check for continuity at x = a
            if f(a - 0.001) == f(a + 0.001):
                print(f"{x}\t\t{f(x)}")
            else:
                print(f"{x}\t\tundefined")
        else:
            print(f"{x}\t\t{f(x)}")

# Test the function with the function f(x) = sqrt(x^2 + 8) if x < 1, -2x + 5 if x > 1
# x  values from 5 to 6
x_values = [x/10 for x in range(50, 61)]


def f(x):
    if x != 6:
        return x**2-3*x-18/x-6
    elif x > 6:
        return 7
    else:
        return None
evaluate_limit_with_table(lambda x: f(6), x_values, 3)


#did not pass but I think it was a logic issue on my part