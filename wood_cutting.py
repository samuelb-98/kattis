import sys
import bisect
costumers = 0
cases = 0
input_nr = 0
case_nr = 0
for line in sys.stdin:
    line = [int(i) for i in line.split()]
    if input_nr == 0:
        cases = line[0]
    if input_nr == 1:
        average = 0
        costumers = line[0]
        work_time = []
    if 1 < input_nr <= costumers + 1:
        bisect.insort(work_time, sum(line[1:]))
    if input_nr == costumers + 1:
        for x in enumerate(work_time):
            average += (costumers-x[0]) / costumers * x[1]
        print(average)
        input_nr = 0
        case_nr +=1
    if case_nr == cases:
        break
    input_nr +=1
