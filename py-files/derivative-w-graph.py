import matplotlib.pyplot as plt

def f(x):
  return 1/4*x**2

def derivative(x, h):
  return (f(x+h) - f(x)) / h

x = -4
h_values = [0.1, 0.01, 0.001, 0.0001]
derivatives = []

for h in h_values:
  derivatives.append(derivative(x, h))

print(derivatives)

x_values = range(-10, 10)
y_values = [f(x) for x in x_values]

plt.plot(x_values, y_values)
plt.show()
