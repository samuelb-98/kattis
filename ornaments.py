from math import acos, pi


while 1:
    r,h,s = tuple(map(int,input().split()))
    if [r,h,s] == [0,0,0]:
        break
    l = (h**2-r**2)**0.5
    a = acos(r/h)
    print("%.2f" % (round((2*l+2*r*(pi-a))*(1+s/100),2)))