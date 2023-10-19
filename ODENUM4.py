from math import sqrt
import matplotlib.pyplot as plt
import numpy as np


def f(x,y):
    return(10**6*y**2)


#a = np.linspace(-1,10,110)
#plt.plot(a,f(a,0))

E = 10**(-7)
x0 = 0
y0 = -E
h = 0.00001
x = []
y = []
c = 10**5

flag = 0


while(y0 < 0):
    k1 = f(x0,y0)
    k2 = f(x0+h/2, y0+h*k1/2)
    k3 = f(x0+h/2, y0+h*k2/2)
    k4 = f(x0+h, y0+h*k3)

    y0 += h/6*(k1+2*k2+2*k3+k4)
    x0 += h
    x.append(x0)
    y.append(y0)
    if y0 > 0:
        print("bruh",x0,y0)
        break

plt.plot(x,y)
plt.grid()
plt.show()