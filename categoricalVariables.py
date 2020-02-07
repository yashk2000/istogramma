import numpy as np
import matplotlib.pyplot as plt

names = ['a', 'b', 'c']
values = [1, 5, 10]

plt.figure(figsize=(12, 4))

plt.subplot(131) # can be written as plt.subplot(1, 3, 1) too
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle("Categorical PLotting")
plt.show()
