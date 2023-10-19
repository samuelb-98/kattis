import math

def dist(p1,p2,p3):
  x0,y0 = p1
  x1,y1 = p2
  x2,y2 = p3

  dy,dx = (y2 - y1), (x2 - x1)
  a, b, c = -1*dy, dx, dy*x1 - dx*y1

  k = float(a**2 + b**2)
  d = abs(a*x0+ b*y0 +c)/math.sqrt(k)

  max_y, min_y, max_x, min_x = max(y1,y2),min(y1,y2),max(x1,x2),min(x1,x2)
  px = (b*(b*x0 - a*y0) - a*c)/k
  py = (a*(-1.0*b*x0 + a*y0) - b*c)/k
  if max_y >= py >= min_y and max_x >= px >= min_x:
    return d

  d1 = math.sqrt((y1-y0)**2 + (x1-x0)**2)
  d2 = math.sqrt((y2-y0)**2 + (x2-x0)**2)
  return min(d1,d2)


    
cases = int(input().strip())
for i in range(cases):
    poly1 = []
    poly2 = []
    n = int(input().strip())
    for i in range(n):
        poly1.append([int(i) for i in input().split()])
    m = int(input().strip())
    for i in range(m):
        poly2.append([int(i) for i in input().split()])

    min_diameter = -1
    for l in range(m):
        for p in poly1:
            p2 = poly2[l]
            p3 = poly2[l-1]
            d = dist(p,p2,p3)
            if d < min_diameter or min_diameter == -1:
                min_diameter = d
    print (min_diameter/2.0)

