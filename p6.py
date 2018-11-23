import numpy as np
from matplotlib import pyplot as plt

def d(n):
	return (n==0)

def u(n):
	return (n>=0)

def x1():
	n = np.array([n for n in range(-10, 11)])
	x = d(n)+d(n-2)
	h = 2*d(n+1)-2*d(n-1)
	y = np.convolve(x,h,'same')
	plt.stem(n, y)
	plt.title('Y1[n]')
	plt.xlabel('n')
	plt.ylabel('Y1[n]')
	plt.show()

def x2():
	n = np.array([n for n in range(0, 25)])
	n2 = np.array([np2 for np2 in range(0, 15)])
	n3 = np.array([np1 for np1 in range(0, 39)])
	x = ((1/2)^(n-2))*u(n-2)
	h = u(n2+2)
	y = np.convolve(x,h)
	plt.stem(n3, y)
	plt.title('Y3[n]')
	plt.xlabel('n')
	plt.ylabel('Y3[n]')
	plt.show()

x1()
