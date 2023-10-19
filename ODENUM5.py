from math import sqrt,exp
import matplotlib.pyplot as plt
import numpy as np


def f(x,y):
    return(y)


#a = np.linspace(-1,10,110)
#plt.plot(a,f(a,0))

E = 0.00000001
x0 = 0
y0 = 52
h = 0.000001
x = []
y = []
k = 1

flag = 0


while(1):
    k1 = f(x0,y0)
    k2 = f(x0+h/2, y0+h*k1/2)
    k3 = f(x0+h/2, y0+h*k2/2)
    k4 = f(x0+h, y0+h*k3)

    y0 += h/6*(k1+2*k2+2*k3+k4)
    x0 += h
    x.append(x0)
    y.append(y0)



    if abs(x0-2**k) < 0.0000001:
        print(k,":", y0,52*exp(2**k))
        if abs(y0-52*exp(2**k)) < 0.01:
            
            k+=1
        else: break

plt.plot(x,y)
plt.grid()
plt.show()