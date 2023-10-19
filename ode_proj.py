import numpy as np
import matplotlib.pyplot as plt


def RK4(f,init,t0,tmax,h):
    X = [(t0,init)]
    x = init
    t = t0
    while t  < tmax:
        k1 = h*f(t,x)
        k2 = h*f(t+h/2, x+k1/2)
        k3 = h*f(t+h/2, x+k2/2)
        k4 = h*f(t+h, x+k3)

        x = x + 1/6*(k1+2*k2+2*k3+k4)
        t += h
        X.append((t,x))
    return(X)


def euler(f,init,t0,tmax,h):
    X = [(t0,init)]
    x = init
    t = t0
    while t < tmax:
        x = x + h*f(t,x)
        t += h
        X.append((t,x))
    return(X)



##########################################################



def existens():
    E = 0.001
    t0 = 0
    tmax = 6
    dt = 0.001
    init = -1 + E
    f = lambda t,y : np.sqrt(abs(y))

    P = (RK4(f,init,t0,tmax,dt))
    x = []
    y = []

    print(min(P, key=lambda x: abs(x[1])))

    for p in P:
        x.append(p[0])
        y.append(p[1])
        

    plt.plot(x,y)
    plt.grid()
    plt.show()


def pang():
    t = 0
    tmax = 100000
    dt = 1
    E = -1
    y = E
    C = 2
    f = lambda t,y : C*y**2

    P = RK4(f,y,t,tmax,dt)
    print(max(P, key=lambda x: x[1]))
    x = []
    y = []
    for p in P:
        x.append(p[0])
        y.append(p[1])
        

    plt.plot(x,y)
    plt.grid()
    plt.show()
def pang2():   
    t = 0
    dt = 0.0001
    y = 0.52
    f = lambda t,y : y**2
    Y = []
    T = []
    while y < 1000:
        y = y + dt*f(t,y)
        t += dt
        T.append(t)
        Y.append(y)
        
    print(t)
    plt.plot(T,Y)
    plt.grid()
    plt.show()

def inte_pang():
    t = 0
    tmax = 100
    h = 0.00001
    y = 52
    f = lambda t,y : y
    k = 1

    while 1:
        k1 = h*f(0,y)
        k2 = h*f(0,y+k1/2)
        k3 = h*f(0,y+k2/2)
        k4 = h*f(0,y+k3)

        y += (k1+2*k2+2*k3+k4)/6
        t += h

        if abs(t-2**k) < h/100:
            v = 52*np.exp(2**k)
            if abs(v - y) < 0.01:
                print(k,":", y, v,"   ", t,2**k)
                k += 1
            else:
                print("fail ",k,":", y, v,"   ", t,2**k)
                break

def pi():
    t = 0
    h = 0.00000001
    x = np.array([1,0])
    f = lambda t,X : np.array([X[1],-X[0]])
    last = 2

    T = [0]
    Y = [1]
    V = [0]

    while 1:
        k1 = h*f(t,x)
        k2 = h*f(t+h/2, x+k1/2)
        k3 = h*f(t+h/2, x+k2/2)
        k4 = h*f(t+h, x+k3)

        x = x + 1/6*(k1+2*k2+2*k3+k4)
        t += h
        
        T.append(t)
        Y.append(x[0])
        V.append(x[1])

        if abs(x[0]) < last:
            last = x[0]
        else:
            print(2*T[-2],":",Y[-2])
            break


def planet_motion(X):
    x,y,vx,vy = X
    r_sq = x**2 + y**2
    GM = 1000
    return(np.array([vx,vy,-GM*x/(r_sq**(3/2)),-GM*y/(r_sq**(3/2))]))
def planet():
    t0 = 0
    tmax = 30
    dt = 0.001
    init = np.array([10,0,0,12])
    f = lambda t,X : planet_motion(X)

    P = RK4(f,init,t0,tmax,dt)

    x = []
    y = []
    for p in P:
        x.append(p[1][0])
        y.append(p[1][1])

    plt.plot(x,y)
    plt.plot(0,0,marker="o",color="y",markersize="20")
    plt.grid()
    plt.show()

def planet_motion2(X):
    xe,ye,vxe,vye, xj,yj,vxj,vyj, xs,ys,vxs,vys = X
    k = -0.1
    return(np.array([vxe,vye,k*xe/(xe**2+ye**2)**(3/2),k*ye/(xe**2+ye**2)**(3/2),
                     vxj,vyj,k*xj/(xj**2+yj**2)**(3/2),k*yj/(xj**2+yj**2)**(3/2),
                     vxs,vys,
                     k*xs/(xs**2+ys**2)**(3/2) + k*abs(xs-xj)/((xs-xj)**2+(ys-yj)**2)**(3/2) + k*abs(xs-xe)/((xs-xe)**2+(ys-ye)**2)**(3/2), 
                     k*ys/(xs**2+ys**2)**(3/2) + k*abs(ys-yj)/((xs-xj)**2+(ys-yj)**2)**(3/2) + k*abs(ys-ye)/((xs-xe)**2+(ys-ye)**2)**(3/2)]))


def revisited():
    t0 = 0
    tmax = 20
    dt = 0.1
    init = np.array([1,0,0,2, 5.2,0,0,10, 1.1,0.1,1,2])
    f = lambda t,X : planet_motion2(X)
    P = RK4(f,init,t0,tmax,dt)

    X1 = [init[0]]
    Y1 = [init[1]]
    X2 = [init[4]]
    Y2 = [init[5]]
    X3 = [init[8]]
    Y3 = [init[9]]
    for p in P:
        X1.append(p[1][0])
        Y1.append(p[1][1])
        X2.append(p[1][4])
        Y2.append(p[1][5])
        X3.append(p[1][8])
        Y3.append(p[1][9])

    print(X1[-1],Y1[-1])

    plt.plot(0,0,marker="o",color="y",markersize="20")
    plt.plot(X1,Y1)
    plt.plot(X2,Y2)
    plt.plot(X3,Y3)
    plt.grid()
    plt.show()

revisited()