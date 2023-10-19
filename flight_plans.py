from collections import deque
import sys

input_nr = 0
direct_flights = []


def broad_search(start,goal,direct_flights):
    search_queue = deque()
    search_queue.append(start)
    distance = [N + 1 for i in range(len(direct_flights))]
    distance[start] = 0
    while len(search_queue) != 0:
        current = search_queue.popleft()
        if current == goal:
            return(distance[goal])
        for nword in direct_flights[current]:
            if distance[nword] == N + 1:
                search_queue.append(nword)
                distance[nword] = distance[current] + 1
    return("impossible")

for line in sys.stdin:
    if input_nr == 0:
        N, start, goal = [int(i) for i in line.split()]
    
    if 1 <= input_nr <= N:
        line = line.split()
        if line[0] == "N":
            line = [int(i) for i in line[2:]]
            direct_flights.append(set(line))

        else:
            line = [int(i) for i in line[2:]]
            direct_flights.append(set([i for i in range(N) if i not in line]))


    if input_nr == N:

        print(broad_search(start,goal,direct_flights))
        
        break

    input_nr += 1

