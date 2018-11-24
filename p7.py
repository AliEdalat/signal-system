import numpy as np
from matplotlib import pyplot as plt

def u(n):
	return (n >= 0)

def x1():
	n = np.array([n for n in range(0, 11)])
	h = (0.9)**n
	n2 = np.array([n2 for n2 in range(0, 100)])
	x = np.cos(n2**2)*np.sin(((2*np.pi)/5)*n2)
	y = np.convolve(x,h)
	n3 = np.array([n3 for n3 in range(0, 110)])
	plt.stem(n3, y)
	plt.title('Y1[n]')
	plt.xlabel('n')
	plt.ylabel('Y1[n]')
	plt.show()

def x3_(x, h, L, N, P):
	xp = np.zeros((L//P, P))
	yp = np.zeros((L//P,N+P-1))
	y = np.zeros(L+P-1)
	for n in range(L//P):
		xp[n, :] = x[n*P:(n+1)*P]
		yp[n, :] = np.convolve(xp[n, :], h, mode='full')
		y[n*P:(n+1)*P+N-1] += yp[n, :]
	y = y[0:N+L]
	return y

def x3():
	n = np.array([n for n in range(0, 11)])
	h = (0.9)**n
	n2 = np.array([n2 for n2 in range(0, 100)])
	x = np.cos(n2^2)*np.sin(((2*np.pi)/5)*n2)
	y = x3_(x,h,100,11,50)
	n3 = np.array([n3 for n3 in range(0, 111)])
	plt.stem(n3, y)
	plt.title('Y3[n]')
	plt.xlabel('n')
	plt.ylabel('Y3[n]')
	plt.show()

def x2():
	n = np.array([n for n in range(0, 11)])
	h = (0.9)**n
	n2 = np.array([n2 for n2 in range(0, 100)])
	x = np.cos(n2^2)*np.sin(((2*np.pi)/5)*n2)
	y0 = np.convolve(x[0:50], h, mode='full')
	y1 = np.convolve(x[50:100], h, mode='full')
	y = [y0[j] + y1[j-50] for j in range(50,110)]
	n3 = np.array([n3 for n3 in range(0, 110)])
	plt.stem(n3, y)
	plt.title('Y2[n]')
	plt.xlabel('n')
	plt.ylabel('Y2[n]')
	plt.show()
	

x2()

