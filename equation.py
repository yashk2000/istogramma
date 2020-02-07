import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)

plt.plot(t, t**3 + 4 * t**2 - 7 * t + 90, '--')
plt.show()