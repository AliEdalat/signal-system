import numpy as np
from matplotlib import pyplot as plt

def x1():
	n = np.array([n for n in range(0, 32)])
	x = (np.cos((np.pi/4) * n))**2
	plt.stem(n, x)
	plt.title('X1(n)')
	plt.xlabel('n')
	plt.ylabel('x1(n)')
	plt.show()

def x2():
	n = np.array([n for n in range(0, 32)])
	x = (np.cos((np.pi/8) * n))*(np.sin((np.pi/4) * n))
	plt.stem(n, x)
	plt.title('X2(n)')
	plt.xlabel('n')
	plt.ylabel('x2(n)')
	plt.show()

def x3():
	n = np.array([n for n in range(0, 49)])
	x = (np.cos((np.pi/3) * n))+3*(np.sin((5*np.pi/12) * n))
	plt.stem(n, x)
	plt.title('X3(n)')
	plt.xlabel('n')
	plt.ylabel('x3(n)')#T=24
	plt.show()

#x1()
#x2()
x3()
