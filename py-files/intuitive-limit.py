def f(x):
  return 3*x-8

def find_delta(epsilon, x, a):
  f_x = f(x)  # calculate the value of f at x
  diff = abs(f_x - a)  # calculate the difference between f(x) and a
  if diff <= epsilon:
    return 0
  else:
    return epsilon / diff

print(find_delta(0.06, 3, -2)) # working example
#change f(x) to slope and change epsilon value and a limit