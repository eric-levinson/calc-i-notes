import sympy

def test_function_limits_at_x_minus_1(f1, f2):
    x = sympy.Symbol('x')

    # Evaluate the limit of f1 as x approaches -1 from the left
    left_limit_f1 = sympy.limit(f1(x), x, 3, dir='-')
    print(f"The limit of f1 as x approaches -1 from the left is {left_limit_f1}.")

    # Evaluate the limit of f2 as x approaches -1 from the left
    left_limit_f2 = sympy.limit(f2(x), x, 3, dir='-')
    print(f"The limit of f2 as x approaches -1 from the left is {left_limit_f2}.")

    if left_limit_f1 == left_limit_f2:
        print("The left limits of the functions are equal.")
    else:
        print("The left limits of the functions are not equal.")

    # Evaluate the limit of f1 as x approaches -1 from the right
    right_limit_f1 = sympy.limit(f1(x), x, 3, dir='+')
    print(f"The limit of f1 as x approaches -1 from the right is {right_limit_f1}.")

    # Evaluate the limit of f2 as x approaches -1 from the right
    right_limit_f2 = sympy.limit(f2(x), x, 3, dir='+')
    print(f"The limit of f2 as x approaches -1 from the right is {right_limit_f2}.")

test_function_limits_at_x_minus_1(lambda x: x**2- 5*x, lambda x: 7*x - 4)