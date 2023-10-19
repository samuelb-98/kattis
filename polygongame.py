from cmath import isclose
import sys
import math
import bisect

def dist(p1,p2):
    return(((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2)**0.5)

def polygonArea(X, Y):
    n = len(X)
    area = 0.0
    j = n - 1
    for i in range(0,n):
        area += (X[j] + X[i]) * (Y[j] - Y[i])
        j = i   
    return float(abs(area / 2.0))

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return(False)

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return (x, y)



print(line_intersection(((0.5,0), (0.5,1)), ((0,0),(1,1))))


n,m = [int(i) for i in input().split()]
poly = []
for i in range(n):
    x,y = [int(i) for i in input().split()]
    poly.append((x,y))

lines = []
line_verts = []
for i in range(m):
    x1,y1,x2,y2 = [float(i) for i in input().split()]
    new = [(x1,y1), (x2,y2)]
    for l in lines:
        ends = (l[0],l[-1])
        new_ends = (new[0],new[-1])
        v = line_intersection(ends,new_ends)
        if v:
            line_verts.append(v)
            d = dist(l[0],v)
            for i,lv in enumerate(l):
                lvd = dist(l[0],lv)
                bisect.insort_left(new,lv, key=dist(new[0],lv))
                if not isclose(lvd,d): 
                    bisect.insort_left(l,v, key=dist(l[0],v))
                

    lines.append(new)

print(lines,line_verts)