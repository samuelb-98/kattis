from math import sqrt
import matplotlib.pyplot as plt
import numpy as np


def f(x,y):
    return(sqrt(abs(y)))


a = np.linspace(-1,10,110)
plt.plot(a, 1/4*a**2)

E = 0.00000001
x0 = -1
y0 = -1+E
h = 0.000001
x = []
y = []
c = 0

flag = 0


while(x0 < 10):
    k1 = f(x0,y0)
    k2 = f(x0+h/2, y0+h*k1/2)
    k3 = f(x0+h/2, y0+h*k2/2)
    k4 = f(x0+h, y0+h*k3)

    y0 += h/6*(k1+2*k2+2*k3+k4)
    x0 += h
    x.append(x0)
    y.append(y0)
    if not flag and y0 > 0.0001:
        print(x0)
        flag = 1

print(x0)

plt.plot(x,y)
plt.grid()
plt.show()