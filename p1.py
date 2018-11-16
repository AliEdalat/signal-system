import numpy as np
from matplotlib import pyplot as plt

def x1():
	n = np.array([n for n in range(0, 32)])
	x = (np.cos((np.pi/4) * n))**2
	plt.stem(n, x)
	plt.title('X1(n) 0 <= n <= 31')
	plt.xlabel('n')
	plt.ylabel('x1(n)')
	plt.show()

x1()
