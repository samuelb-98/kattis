from math import sqrt,exp
import matplotlib.pyplot as plt
import numpy as np





def f1(t,x,y):
    return t
def f2(t,x,y):
    return -x

h = 0.01
x0 = 0
y0 = 1
t0 = 0


while(1):
    k1 = f(x0,y0)
    k2 = f(x0+h/2, y0+h*k1/2)
    k3 = f(x0+h/2, y0+h*k2/2)
    k4 = f(x0+h, y0+h*k3)

    y0 += h/6*(k1+2*k2+2*k3+k4)
    x0 += h
    x.append(x0)
    y.append(y0)
