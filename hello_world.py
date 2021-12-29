import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, -5, 5])

for i in range(50):
    x = np.random.uniform(0,10)
    y = np.sin(x)
    plt.scatter(x, y)
    plt.pause(0.05)

plt.show()