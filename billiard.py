import sys
from math import sqrt,atan,degrees

def hyp(a,b):
    return sqrt(a**2 + b**2)


for line in sys.stdin:
    if line.strip() == "0 0 0 0 0":
        break
    else:
        a,b,s,m,n = [int(i) for i in line.split()]
        vel = hyp(a*m,b*n)/s
        x = abs(degrees(atan((b*n)/(a*m))))
        print("%.2f" % x,"%.2f" % vel)
