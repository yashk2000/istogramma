import matplotlib.pyplot as plt
import numpy as np

def found_fit(x):
    return 2 * x**2

x_data = list(range(10))
y_data = []
for i in range(1, 11):
    y_data.append(found_fit(i))

x_func = np.linspace(0, 10)
y_func = found_fit(x_func)

plt.scatter(x_data, y_data, c='g', label = "data")
plt.plot(x_func, y_func, label='$f(x) = 2 x^2$')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Squares")
plt.legend()
plt.show()