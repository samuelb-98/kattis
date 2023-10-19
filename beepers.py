import sys


def dist(a,b):
    return(abs(a[0]-b[0]) + abs(a[1]-b[1]))

def minimal_cycle(start, points, visited):
  def min_cycle_recursive(current, visited):
    if ~ visited == 0:
      return dist(start, current)
    min_val = 800
    for i in range(len(points)):
      if visited & (1 << i) == 0 :
        visited = visited ^ (1 << i)
        ret_val = min_cycle_recursive(points[i], visited)
        cur_val = dist(current, points[i]) + ret_val
        if cur_val < min_val:
          min_val = cur_val
        visited = visited & (~ (1 << i))
        return(min_val)
    visited = visited & (~1)
    return min_cycle_recursive(points[0], visited)

input_nr = 0
cases = -1
case = 0
nr_beepers = -10
for line in sys.stdin:
    line = [int(i) for i in line.split()]
    if input_nr == 0:
        cases = line[0]
    if input_nr == 1:
        dimensions = line
        beepers = []
        visited = ~ ((2**(num_points+1)) - 1)
    if input_nr == 2:
        start = line
    if input_nr == 3:
        nr_beepers = line[0]
    if 3 < input_nr <= nr_beepers + 3:
        beepers.append(line)
    if input_nr == nr_beepers + 3:
        minimal_cycle(start, beepers, visited)

        input_nr = 0
        case +=1
    if case == cases:
        break
    input_nr +=1