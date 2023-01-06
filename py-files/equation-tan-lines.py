import matplotlib.pyplot as plt

def f(x):
  return x**4

x0 = -2
y0 = f(x0)
derivative = -32

def tangent_line(x):
  return derivative * (x - x0) + y0

x_values = range(-10, 10)
y_values = [f(x) for x in x_values]
tangent_y_values = [tangent_line(x) for x in x_values]

plt.plot(x_values, y_values)
plt.plot(x_values, tangent_y_values)
plt.show()

#ended up guessing and getting it write based of chatgpt
#updated the code after correcting chatgpt