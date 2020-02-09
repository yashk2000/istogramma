import boost_histogram as bh
import numpy as np
import matplotlib.pyplot as plt

hist = bh.Histogram(bh.axis.Regular(bins=10, start=0, stop=1))
ar = hist.view()
plt.plot(ar)
plt.show()