import numpy as np
from matplotlib import pyplot as plt

def x1():
	no = np.array([n for n in range(0, 31)])
	x = no + ((np.sin(((np.pi*2)/5)*no)*5)/(2*np.pi))
	plt.stem(no, x)
	plt.title('Y2[n]')
	plt.xlabel('x[n]')
	plt.ylabel('Y2[n]')
	plt.show()
def x2():
	no = np.array([n for n in range(0, 31)])
	x = 3*no + ((np.sin(((np.pi*2))*no))/(2*np.pi)) + ((np.sin(((np.pi*5)/3)*no)*6)/(5*np.pi)) + ((np.sin(((np.pi)/3)*no)*6)/(np.pi))
	plt.stem(no, x)
	plt.title('Y2[n]')
	plt.xlabel('x[n]')
	plt.ylabel('Y2[n]')
	plt.show()
x2()
