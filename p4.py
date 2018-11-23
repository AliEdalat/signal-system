import numpy as np
from matplotlib import pyplot as plt

def heaviside(t):
	return (t>=0) * 1;
def f(t):
	return t*(heaviside(t) - heaviside(t-2))

t = np.arange(-2,6,0.1)
plt.plot(t, f(-2*t+1))
plt.show()
