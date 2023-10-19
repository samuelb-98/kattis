
import math, sys


def ccw(x1,y1,x2,y2,x3,y3):
    return (y3-y1) * (x2-x1) > (y2-y1) * (x3-x1)

def intersect(x1,y1,x2,y2,x3,y3,x4,y4):
    return ccw(x1,y1,x3,y3,x4,y4) != ccw(x2,y2,x3,y3,x4,y4) and ccw(x1,y1,x2,y2,x3,y3) != ccw(x1,y1,x2,y2,x4,y4)    


def dist(p1,p2,p3):
    x0,y0 = p1
    x1,y1 = p2
    x2,y2 = p3

    dy,dx = (y2 - y1), (x2 - x1)
    a, b, c = -1*dy, dx, dy*x1 - dx*y1

    k = float(a**2 + b**2)
    if k == 0.0:
        return(math.sqrt((x0-x1)**2 + (y0-y1)**2))
    else:
        d = abs(a*x0+ b*y0 +c)/math.sqrt(k)

    max_y, min_y, max_x, min_x = max(y1,y2),min(y1,y2),max(x1,x2),min(x1,x2)
    px = (b*(b*x0 - a*y0) - a*c)/k
    py = (a*(-1.0*b*x0 + a*y0) - b*c)/k
    if max_y >= py >= min_y and max_x >= px >= min_x:
        return d

    d1 = math.sqrt((y1-y0)**2 + (x1-x0)**2)
    d2 = math.sqrt((y2-y0)**2 + (x2-x0)**2)
    return min(d1,d2)


innr = 0
cases = 0
for line in sys.stdin:
    if innr == 0:
        cases = int(line.strip())
    if 0 < innr <= cases:
        x1,y1,x2,y2,x3,y3,x4,y4 = [int(i) for i in line.split()]
        ans = 100000
        if intersect(x1,y1,x2,y2,x3,y3,x4,y4):
            ans = 0.0
        else:
            d = dist([x1,y1],[x3,y3],[x4,y4])
            if d < ans:
                ans = d
            d = dist([x2,y2],[x3,y3],[x4,y4])
            if d < ans:
                ans = d
            d = dist([x3,y3],[x1,y1],[x2,y2])
            if d < ans:
                ans = d
            d = dist([x4,y4],[x1,y1],[x2,y2])
            if d < ans:
                ans = d
        print("{:.2f}".format(round(ans, 2)))
    if innr == cases:
        break
    innr += 1