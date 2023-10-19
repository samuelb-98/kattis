import sys

innr = 0
for line in sys.stdin:
    line = [int(i) for i in line.split()]
    if innr == 0:
        N,M,A,K = line
        roads = [[] for x in range(N)]
        danger = [False for x in range(N)]
        print(roads)

    if 0 < innr <= M:
        roads[line[0]-1].append((line[1],line[2]))
        roads[line[1]-1].append((line[0],line[2]))
        print(roads)
    #if innr == M:
    #    print(roads)

    if M < innr <= M + A:
        visited = [False for x in range(N)]
        danger[line-1] = (True,0)

        

    if innr == M + A:
        pass

    innr +=1

    