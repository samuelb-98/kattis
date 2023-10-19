import sys
N = 0
input_nr = 0
case_nr = 1
for line in sys.stdin:
    line = line.split()
    if input_nr == 0:
        cases = int(line[0])
    if input_nr == 1:
        N = int(line[0])
        wares = dict()
    if 1 < input_nr <= N + 1:
        if line[0] in wares:
            wares[line[0]] += int(line[1])
        else:
            wares[line[0]] = int(line[1])
    if input_nr == N + 1:
        ship = []
        for toy in wares:
            ship.append((toy, wares[toy]))
        ship = (sorted(ship,key=lambda sl: (-sl[1],sl[0])))


        print(len(ship))
        for i in ship:
            print(i[0],i[1])
        input_nr = 0
        case_nr +=1
    if case_nr == cases+1:
        break
    input_nr +=1

