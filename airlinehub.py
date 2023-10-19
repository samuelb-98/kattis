import sys
from math import acos,sin,cos,radians,degrees


def find_angle(p,q):
    return(acos(sin(p[0])*sin(q[0]) + cos(p[0])*cos(q[0])*cos(abs(p[1]-q[1]))))


def find_min_max(coords):
    furthest = [0 for i in range(len(coords))]
    for i,p in enumerate(coords):
        for j,q in enumerate(coords[i+1:]):
            a = find_angle(p,q)
            if a > furthest[i]:
                furthest[i] = a
            if a > furthest[i+j+1]:
                furthest[i+j+1] = a
    return(furthest.index(min(furthest)))
            




n = -1
innr = 0
for line in sys.stdin:
    if innr == 0:
        n = int(line.strip())
        coords = []
        incoords = []
    if 0 < innr <= n:
        incoords.append(tuple([float(i) for i in line.split()]))
        coords.append(tuple([radians(float(i)) for i in line.split()]))
    if innr == n:
        index = find_min_max(coords)
        lat = incoords[index][0]
        lon = incoords[index][1]
        print("%.2f" % lat,"%.2f" % lon)
        innr = -1
    innr +=1

