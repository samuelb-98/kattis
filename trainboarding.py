import sys


input_nr = 1
for line in sys.stdin:
    if input_nr == 1:
        N, L, P = [int(i) for i in line.split()]
        longest_walk = 0
        cars = [0]*N    
    if 1 < input_nr <= P+1:
        pos = int(line.split()[0])
        if pos >= N * L:
            closest_car = -1
            walk = pos - N * L + L//2
        else:
            walk = abs(L//2 - pos%L)
            closest_car = pos//L

        cars[closest_car] += 1
        if longest_walk < walk:
            longest_walk = walk

    input_nr +=1
    if input_nr == P+2:
        print(longest_walk)
        print(max(cars))
        break

