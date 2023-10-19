import sys


input_nr = 0
n = -1
for line in sys.stdin:
    line = [int(i) for i in line.split()]
    if input_nr == 0:
        n = line[0]
        avg = 0
    if 0 < input_nr <= n:
        avg += (line[1]-line[0])/n
    if input_nr == n:
        print(avg)
    input_nr +=1