import sys
import heapq
from math import sqrt


def distance(p1,p2):
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def find_dists(points):
    dists = [[0.0]*len(points) for d in range(len(points))] 
    for i,p1 in enumerate(points):
        for j,p2 in enumerate(points[i+1:]):
            d = distance(p1,p2)
            dists[i][i+j+1] = d
            dists[i+j+1][i] = d
    return dists


nr_points = 3
innr = 0
canr = 0
for line in sys.stdin:
    if innr == 0:
        cases = int(line.strip())
    if innr == 2:
        nr_points = int(line.strip())
        points = []
        found = [False for i in range(nr_points)]
        total = 0
        counter = 0
        remaining = set(range(nr_points))
        closest = [0]*nr_points
    if 2 < innr <= 2 + nr_points:
        point = tuple([float(i) for i in line.split()])
        points.append(point)

    if innr == 2+nr_points:
        dists = find_dists(points)
        found[0] = True
        q = []
        for p in range(1,nr_points):
            heapq.heappush(q,(dists[0][p],p))
            closest[p] = dists[0][p]
        while counter < nr_points - 1:
            while True:
                d,point = heapq.heappop(q)
                if found[point]:
                    continue
                break
            total += d
            found[point] = True
            counter +=1
            remaining.remove(point)
            for i in remaining:
                if dists[point][i] < closest[i]:
                    closest[i] = dists[point][i]
                    heapq.heappush(q,(dists[point][i],i))
            
        canr += 1
        print("%.2f" % total)
        innr = 0
        
    if canr == cases:
        break
    innr +=1