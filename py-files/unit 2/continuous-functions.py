def f(x):
    if x < -4:
        return (x + 3)**2 - 2
    elif x >= -4:
        return 5 * (x + 12)
    else:
        return None

x = -4

left_sided_limit = (x + 3)**2 - 2
right_sided_limit = 5 * (x + 12)

if left_sided_limit is None or right_sided_limit is None:
    print("not continuous at x =", x, "because f(x) is undefined")
elif left_sided_limit == right_sided_limit:
    print("Continuous at x =", x)
else:
    print("not continuous at x =", x, "because the limit as x ->", x, "of f(x) does not exist")
#good luck