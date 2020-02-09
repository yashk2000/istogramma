import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)
print(plt.style.available)

plt.figure(1)
plt.style.use('fivethirtyeight')
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^', t, t**t, '--')

plt.figure(2)
plt.style.use('seaborn-ticks')
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^', t, t**t, '--')

plt.figure(3)
plt.style.use('ggplot')
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^', t, t**t, '--')

plt.figure(4)
plt.style.use('dark_background')
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^', t, t**t, '--')

plt.figure(5)
plt.style.use('bmh')
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^', t, t**t, '--')

plt.figure(6)
plt.style.use('seaborn-poster')
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^', t, t**t, '--')

plt.figure(7)
plt.style.use('seaborn-notebook')
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^', t, t**t, '--')

plt.figure(8)
plt.style.use('fast')
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^', t, t**t, '--')

plt.figure(9)
plt.style.use('seaborn')
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^', t, t**t, '--')

plt.figure(10)
plt.style.use('classic')
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^', t, t**t, '--')

plt.figure(11)
plt.style.use('Solarize_Light2')
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^', t, t**t, '--')

plt.figure(12)
plt.style.use('seaborn-ticks')
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^', t, t**t, '--')

plt.figure(13)
plt.style.use('seaborn-ticks')
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^', t, t**t, '--')

plt.figure(14)
plt.style.use('seaborn-ticks')
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^', t, t**t, '--')

plt.show()