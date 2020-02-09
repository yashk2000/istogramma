import boost_histogram as bh
import numpy as np
import matplotlib.pyplot as plt

hist3D = bh.Histogram(
    bh.axis.Regular(10, 0, 100),
    bh.axis.Regular(10, 0.0, 10.0),
    bh.axis.Variable([1,2,3,4,5,5.5,6])
)

ar = hist3D.to_numpy(flow=False)
print(ar)
plt.plot(ar[1], ar[2], ar[3])#, ar[0])
plt.show()
