from math import sqrt,exp
import matplotlib.pyplot as plt
import numpy as np

G = 6.67*10**(-11)
M = 2*10**30
GM = 1000

def f1(t,x,y,vx,vy):
    return vx
def f3(t,x,y,vx,vy):
    return(-GM*x/((x**2+y**2)**(3/2)))
def f2(t,x,y,vx,vy):
    return vy
def f4(t,x,y,vx,vy):
    return (-GM*y/((x**2+y**2)**(3/2)))


h = 0.01
t0 = 0
x0 = 10
y0 = -5
vx0 = 0
vy0 = 12
tmax = 4000

X = []
Y = []
VX = []
VY = []

t,x,y,vx,vy = t0,x0,y0,vx0,vy0

while(t < tmax):
    k1x = f1(t,x,y,vx,vy)
    k1y = f2(t,x,y,vx,vy)
    k1vx = f3(t,x,y,vx,vy)
    k1vy = f4(t,x,y,vx,vy)

    k2x = f1(t+h/2,x+h/2*k1x,y+h/2*k1y,vx+h/2*k1vx,vy+h/2*k1vy)
    k2y = f2(t+h/2,x+h/2*k1x,y+h/2*k1y,vx+h/2*k1vx,vy+h/2*k1vy)
    k2vx = f3(t+h/2,x+h/2*k1x,y+h/2*k1y,vx+h/2*k1vx,vy+h/2*k1vy)
    k2vy = f4(t+h/2,x+h/2*k1x,y+h/2*k1y,vx+h/2*k1vx,vy+h/2*k1vy)

    k3x = f1(t+h/2,x+h/2*k2x,y+h/2*k2y,vx+h/2*k2vx,vy+h/2*k2vy)
    k3y = f2(t+h/2,x+h/2*k2x,y+h/2*k2y,vx+h/2*k2vx,vy+h/2*k2vy)
    k3vx = f3(t+h/2,x+h/2*k2x,y+h/2*k2y,vx+h/2*k2vx,vy+h/2*k2vy)
    k3vy = f4(t+h/2,x+h/2*k2x,y+h/2*k2y,vx+h/2*k2vx,vy+h/2*k2vy)

    k4x = f1(t+h,x+h*k3x,y+h*k3y,vx+h*k3vx,vy+h*k3vy)
    k4y = f2(t+h,x+h*k3x,y+h*k3y,vx+h*k3vx,vy+h*k3vy)
    k4vx = f3(t+h,x+h*k3x,y+h*k3y,vx+h*k3vx,vy+h*k3vy)
    k4vy = f4(t+h,x+h*k3x,y+h*k3y,vx+h*k3vx,vy+h*k3vy)
  
    t += h
    x += h/6*(k1x + 2*k2x + 2*k3x + k4x)
    y += h/6*(k1y + 2*k2y + 2*k3y + k4y)
    vx += h/6*(k1vx + 2*k2vx + 2*k3vx + k4vx)
    vy += h/6*(k1vy + 2*k2vy + 2*k3vy + k4vy)


    if x**2 + y**2 < 2:
        break

    X.append(x)
    Y.append(y)
    VX.append(vx)
    VY.append(vy)


print(x,y)

plt.plot(X,Y)
plt.plot(0,0,marker="o",color="y",markersize="20")
plt.grid()
plt.show()