import sys
cases = 0
input_nr = 0
for line in sys.stdin:
    if line.strip() == "0":
        break
    if input_nr == 0:
        nr_edges = int(line.strip())
        points = []
    if 0 < input_nr <= nr_edges:
        points.append(tuple([int(i) for i in line.split()]))
    if input_nr == nr_edges:
        area = 0
        for i in range(len(points)-1):
            area += (points[i][0]*points[i+1][1] - points[i+1][0]*points[i][1])
        area = area + (points[-1][0]*points[0][1] - points[-1][1]*points[0][0])
        if area < 0:
            direction = "CW"
        else:
            direction = "CCW"
        print(direction, round(abs(area/2),1))    
        input_nr = -1
    input_nr +=1