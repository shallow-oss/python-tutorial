import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])
plt.plot(x, y)

plt.title("TITLE")
plt.xlabel("x - label")
plt.ylabel("y - label")

plt.show()
