import sys
import bisect

INF = 100000

def slope_sort(p,list):
    out_list = []
    for point in list:
        if point == p:
            continue
        if point[0] == p[0]:
            if point[1] < p[1]:
                slope = - INF
            else:
                slope = INF
        else:
            slope = (point[1]-p[1]) / (point[0]-p[0])
        bisect.insort(out_list, (slope, point))
    return out_list

def cross_product(s2,s1,p):
    cross = (p[0]-s1[0]) * (s2[1]-s1[1]) - (p[1]-s1[1]) * (s2[0]-s1[0])
    return(cross)

nr_points = 0
input_nr = 0

for line in sys.stdin:
    line = [int(i) for i in line.split()]
    if line == [0]:
        break

    if input_nr == 0:
        nr_points = line[0]
        points = []
        min_x = INF
        min_x_index = ""
        hull_points = []

    if 0 < input_nr <= nr_points:
        points.append(tuple(line))
        if line[0] == min_x:
            if line[1] < points[min_x_index][1]:
                min_x = line[0]
                min_x_index = input_nr - 1
        if line[0] < min_x:
            min_x = line[0]
            min_x_index = input_nr - 1
    
    if input_nr == nr_points:
        P0 = points.pop(min_x_index)
        hull_points.append(P0)
        points = slope_sort(P0, points)
        for point in points:
            while len(hull_points) > 1 and cross_product(hull_points[-2], hull_points[-1], point[1]) <= 0:
                hull_points.pop()
            hull_points.append(point[1])
        print(len(hull_points))
        for i in hull_points:
            print(i[0],i[1])
        input_nr = -1
    input_nr +=1