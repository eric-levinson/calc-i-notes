import matplotlib.pyplot as plt

def f(x):
  return -2*x**2

def derivative(x, h):
  return (f(x+h) - f(x)) / h

x_values = range(-10, 10)
derivatives = []

for x in x_values:
  h = 0.01
  derivative_at_x = derivative(x, h)
  derivatives.append(derivative_at_x)

print("x:", x_values)
print("f'(x):", derivatives)

y_values = [f(x) for x in x_values]

plt.plot(x_values, y_values)
plt.show()
#this is not useful, don't recommend using during exam