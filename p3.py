import numpy as np
from matplotlib import pyplot as plt

def u(n):
	return (n >= 0)

def x2():
	n = np.array([n for n in range(-5, 10)])
	plt.stem(n, u(n))
	plt.title('U[n]')
	plt.xlabel('n')
	plt.ylabel('U[n]')
	plt.show()
	no = np.array([n for n in range(-6, 10)])
	x = u(no) + u(no+1)
	plt.stem(no, x)
	plt.title('Y2[n]')
	plt.xlabel('x[n]')
	plt.ylabel('Y2[n]')
	plt.show()

def x3():
	n = np.array([n for n in range(-50, 51)])
	x = np.log(np.exp(n))
	plt.stem(n, x)
	plt.title('Y2[n]')
	plt.xlabel('x[n]')
	plt.ylabel('Y2[n]')
	plt.show()

x3()