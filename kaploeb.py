import sys

INF = 10000
l = -1
innr = 0
for line in sys.stdin:
    if innr == 0:
        l,k,s = [int(i) for i in line.split()]
        time = [0 for i in range(s)]
        laps = [0 for i in range(s)]
        order = []
    if 0 < innr <= l:
        r,t = line.split()
        r = int(r) - 1
        t = int(t.split(".")[0])*60 + int(t.split(".")[1])

        laps[r] +=1
        time[r] += t

        if innr == l:
            order = sorted(range(1,s+1), key = lambda k : time[k-1])
            for r in order:
                if laps[r-1] == k:
                    print(r)
            break
    innr +=1