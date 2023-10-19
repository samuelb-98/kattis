import sys

connections = {}

input_nr = 0
for line in sys.stdin:
    if input_nr == 0:
        N = int(line.split()[0])
    if 1 <= input_nr <= N:
        input = line.split()
        if input[0] in connections:
            for station in input[1:]:
                connections[input[0]].add(station)
        else:
            connections[input[0]] = set(input[1:])
        for station in input[1:]:
            if station in connections:
                connections[station].add(input[0])
            else:
                connections[station] = {input[0]}
            
    input_nr += 1
    if input_nr == N + 2:
        start, goal = line.split()
        break


visited = [start]
q = [start]
prev = dict()
for station in connections:
    prev[station] = 0


while len(q) != 0:
    current_station = q.pop(0)
    for next_station in connections[current_station]:
        if next_station not in visited:
            q.append(next_station)
            prev[next_station] = current_station
            visited.append(next_station)
if prev[goal] == 0:
    print("no route found")
    
else:    
    path = [goal]
    current = goal
    while current != start:
        path.append(prev[current])
        current = prev[current]

    path.reverse()
    print(' '.join(map(str, path)))
