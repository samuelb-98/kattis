import sys


def dist(p1,p2):
    return(((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5)

def connected(c1,c2):
    if abs(c1[2] - c2[2]) < dist(c1[:2],c2[:2]) < c1[2] + c2[2] or c1 == c2:
        return(True)
    else:
        return(False)

def find_largest(circles):
    largest = 0
    visited = []
    for start in circles:
        if start in visited:
            continue
        q = [start]
        visited.append(start)
        step = 0
        while q != []:
            curr = q.pop()
            step +=1
            for c in circles:
                if connected(c,curr) and c not in visited:
                    q.append(c)
                    visited.append(c)
        if largest < step:
            largest = step
        return(largest)
                


nr_circles = 0
input_nr = 0
for line in sys.stdin:
    if line.strip() == "-1":
        break
    if input_nr == 0:
        nr_circles = int(line.strip())
        circles = []
    if 0 < input_nr <= nr_circles:
        circles.append([float(i) for i in line.split()])
    if input_nr == nr_circles:
        largest = find_largest(circles)
        if largest == 1:
            print(f"The largest component contains {largest} ring.")
        else:
            print(f"The largest component contains {largest} rings.")
        input_nr = -1
    input_nr +=1