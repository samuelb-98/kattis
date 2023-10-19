import sys
import bisect

def timer(start,sacks,cd,s):
    pos = start
    time = 0
    while len(sacks) > 0:
        pos = pos%s
        print(sacks,pos,time)
        if pos in sacks:
            sacks.remove(pos)
            time += cd
            pos += cd
        else:
            next_pos = sacks[bisect.bisect_left(sacks, pos) % len(sacks)]
            if next_pos < pos:
                time += s 
            time += next_pos - pos
            pos = next_pos

    return(time)

def find_slowest(time_map,s):
    slowest = -1
    for i in range(len(time_map[:-1])):
        time = time_map[i+1][1] + time_map[i+1][0] - time_map[i][0]
        if time > slowest:
            slowest = time
    time = time_map[0][1] + time_map[0][0] 



input_nr = 0
for line in sys.stdin:
    line = [int(i) for i in line.split()]
    if input_nr == 0:
        n,s,t = line
    if input_nr == 1:
        positions = sorted(line)
        print(positions)
        uniques = set(positions)
        times = []
        time_map = []
        for sack in uniques:
            time_map.append((sack,timer(sack,positions.copy(),t,s)))
        print(time_map)
    input_nr +=1