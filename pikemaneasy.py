import sys
from bisect import insort
first = True
total_time = 0
solution_times = []

def next_time(previous_time, A, B, C):
    t_next = ((A * previous_time + B) % C) + 1
    return(t_next)


def find_lowest_penalty(solutiuon_times):
    penalty = 0
    for time in enumerate(solution_times):
        penalty += sum(solution_times[:time[0] + 1])
        penalty = penalty % 1000000007
    return(penalty)
        

for line in sys.stdin:
    line = [int(i) for i in line.split()]
    if first:
        N, T = line
    else:
        A, B, C, t0 = line
        break
    first = False

previous_time = t0
total_problems = 0
while total_time + previous_time <= T and total_problems < N:
    total_time += previous_time
    total_problems += 1
    insort(solution_times, previous_time)
    previous_time = next_time(previous_time, A, B, C)

print(solution_times)
print(total_problems, find_lowest_penalty(solution_times))
