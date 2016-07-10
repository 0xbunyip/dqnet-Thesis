import numpy as np
import matplotlib.pyplot as plt

np.random.seed(333)

# example data
x = np.random.rand()
y = np.exp(-x)

# First illustrate basic pyplot interface, using defaults where possible.
plt.figure()
plt.errorbar(x, y, xerr=0.2, yerr=0.4, fmt='o')
plt.title("Simplest errorbars, 0.2 in x, 0.4 in y")
plt.show()