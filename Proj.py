import numpy as np
import matplotlib.pyplot as plt
import math

def RK4(f,init,t0,tmax,h):
    #RK4 implementation, tar in funktioner, initialvärden för funktioner, initial oberoende variabel, ev max oberoende variabel samt step size. 
    #Matar ut en array av vectorer på formen (oberoende variabel,vector av funtionsvärden)
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
    #euler fram med samma in och ut som RK4
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
    E = 0.007
    t0 = 0
    tmax = 6
    dt = 0.0001
    init = -1 
    f = lambda t,y : np.sqrt(abs(y))

    P = (euler(f,init,t0,tmax,dt))
    x = []
    y = []


    flag = 0
    for p in P:
        x.append(p[0])
        y.append(p[1])
        if flag == 0 and abs(p[1]) < 10**(-4):
            flag = 1
            x0 = p[0]
        if flag == 1 and abs(p[1]) > 10**(-4):
            flag = -1
            print(x0,p[0], p[0]-x0)

    plt.plot(x,y)
    plt.grid()
    plt.show()

def pang():
    t = 0
    tmax = 2
    dt = 0.00001
    y = 0.52
    f = lambda t,y : y**2

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
    while y < 10**20:
        y = y + dt*f(t,y)
        t += dt
        T.append(t)
        Y.append(y)
        
    print(t)
    plt.plot(T,Y)
    plt.grid()
    plt.show()
def pang3():
    t = 0
    tmax = 2
    dt = 1
    E =1000
    y0 = -2
    C = 1
    f = lambda t,y : C*y**2

    P = RK4(f,y0,t,tmax,dt)
    print(max(P, key=lambda x: x[1]))
    x = []
    y = []
    for p in P:
        x.append(p[0])
        y.append(p[1])
        

    plt.plot(x,y)
    plt.grid()
    plt.show()

def inte_pang():
    t = 0
    tmax = 100
    h = 0.000001
    y = 52
    f = lambda t,y : y
    k = 1
    prev = 0

    while 1:
        k1 = h*f(0,y)
        k2 = h*f(0,y+k1/2)
        k3 = h*f(0,y+k2/2)
        k4 = h*f(0,y+k3)
        
        prevy = y
        prevt = t
        y += (k1+2*k2+2*k3+k4)/6
        t += h

        if t > 32.1:
            print("bruh")
            break

        if t > 2**k:
            if abs(t-2**k) < abs(prevt-2**k):
                
                prevt = t
                prevy = y 
            v = 52*np.exp(2**k)
            if abs(v - prevy) < 0.01:
                print(k,":", prevy, v,"   ", t,2**k)
                k += 1
            else:
                print("fail ",k,":", y, v,"   ", t,2**k)
                break

def pi():
    t = 0
    h = 0.001
    x = np.array([1,0])
    f = lambda t,X : np.array([X[1],-X[0]])
    last = 2
    counter = 0
    test = []


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

        if x[0] < 0:
            if abs(Y[-1]) < abs(Y[-2]):
                print(2*T[-1],)

    print(test)

    plt.plot(T,Y)
    plt.grid()
    plt.show()

def planet_motion(X):
    x,y,vx,vy = X
    r_sq = x**2 + y**2
    GM = 1000
    return(np.array([vx,vy,-GM*x/(r_sq**(3/2)),-GM*y/(r_sq**(3/2))]))
def planet():
    t0 = 0
    tmax = 2000
    dt = 0.01
    init = np.array([10,0,0,12])
    f = lambda t,X : planet_motion(X)

    P = euler(f,init,t0,tmax,dt)

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
    G = -39.48/365**2
    S = 1
    J = 0.0009543
    E = 3*10**-6
    return(np.array([vxe,vye,G*S*xe/(xe**2+ye**2)**(3/2),G*S*ye/(xe**2+ye**2)**(3/2),
                     vxj,vyj,G*S*xj/(xj**2+yj**2)**(3/2),G*S*yj/(xj**2+yj**2)**(3/2),
                     vxs,vys,
                     (G*S*xs/(xs**2+ys**2)**(3/2) + 1*G*J*abs(xs-xj)/((xs-xj)**2+(ys-yj)**2)**(3/2) + G*E*abs(xs-xe)/((xs-xe)**2+(ys-ye)**2)**(3/2)), 
                     (G*S*ys/(xs**2+ys**2)**(3/2) + 1*G*J*abs(ys-yj)/((xs-xj)**2+(ys-yj)**2)**(3/2) + G*E*abs(ys-ye)/((xs-xe)**2+(ys-ye)**2)**(3/2))]))
def revisited():
    t0 = 0
    tmax = 5000
    dt = 0.01
    init = np.array([1,0,0,0.017, -0.7636,5,-0.007,0, 1.01,0,0,0.024])
    f = lambda t,X : planet_motion2(X)
    P = RK4(f,init,t0,tmax,dt)

    X1 = [init[0]]
    Y1 = [init[1]]
    X2 = [init[4]]
    Y2 = [init[5]]
    X3 = [init[8]]
    Y3 = [init[9]]

    dsj = 5
    for p in P:
        d = ((p[1][4]-p[1][8])**2 + (p[1][5]-p[1][9])**2)**0.5
        if d < dsj:
            dsj = d

        X1.append(p[1][0])
        Y1.append(p[1][1])
        X2.append(p[1][4])
        Y2.append(p[1][5])
        X3.append(p[1][8])
        Y3.append(p[1][9])

    print(dsj)

    plt.plot(0,0,marker="o",color="y",markersize="20")
    plt.plot(X1,Y1)
    plt.plot(X2,Y2)
    plt.plot(X3,Y3)
    plt.grid()
    plt.show()


#existens()
#pang()
#pang2()
#pang3()
inte_pang()
#pi()
#planet()
#revisited()



