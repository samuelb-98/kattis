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


def euler(f,x0,t0,tmax,h):
    t = np.arange(t0,tmax+h,h)
    X = np.zeros((x0.size,t.size))
    X[:,0] = x0
    for i in range(t.size-1):
        dx = h*f(t[i],X[:,i])
        X[:,i+1] = X[:,i] + dx

    return(X,t)



"""uppgift 1"""
def f1(x,d,vmax,g,M):
    out = np.zeros(M)
    for i in range(M-1):
        dist = x[i+1]-x[i]
        if dist > d:
            out[i] = vmax
        else:
            out[i] = dist*vmax/d
    out[-1] = g
    return(out)


def uppgift2():
    d = 75
    vmax = 25
    M = 10
    g = 5
    x0 = np.zeros(M)
    for i in range(M):
        x0[i] = d*(i+1)

    f = lambda t,x : f1(x,d,vmax,g,M)

    t0 = 0
    tmax = 40
    h = 1

    P,T = euler(f,x0,t0,tmax,h)

    for i in range(M):
        plt.plot(P[i],T)
    plt.grid()
    plt.show()


def uppgift3():
    d = 75
    vmax = 25
    M = 10
    g = 25
    x0 = np.zeros(M)
    for i in range(M):
        x0[i] = 10*(i+1)

    f = lambda t,x : f1(x,d,vmax,g,M)

    t0 = 0
    tmax = 40
    h = 0.1

    P,T = euler(f,x0,t0,tmax,h)

    for i in range(T.size):
        for j in range(x0.size):
            plt.plot(P[j][i],0,marker="o",color="g",markersize="10")
        plt.pause(h)
        plt.clf()
    plt.show


def uppgift4():
    h = 1
    d = 75
    v = 25
    M = 10
    g = 5
    x = np.zeros(M)
    for i in range(M):
        x[i] = 75*(i+1)

    t = np.arange(0,40,h)
    P = np.zeros((M,t.size))


    for j in range(t.size):
        x[-1] += h*g
        for i in range(2,M+1):
            x[-i] = (x[-i] + h*v/d*x[-i+1])/(1+h*v/d)
        P[:,j] = x


    for i in range(M):
        plt.plot(P[i],t)
    plt.grid()
    plt.show()


def uppgift7():
    