import sys

def overlap(a,b):
    if a[1] < b[0] or a[0] > b[1] or b[1] < a[0] or b[0] > a[1]:
        return(False)
    else:
        return(True)

times = dict()
input_nr = 0
N = -1
for line in sys.stdin:
    if input_nr == 0:
        N,D = [int(i) for i in line.split()]
    if input_nr == 1:
        infected = [int(i) for i in line.split()[1:]]
        healthy = [i for i in range(1,N+1)]
        for i in infected:
            healthy.remove(i)
    if 1 < input_nr <= N+1:
        times[input_nr-1] = [int(i) for i in line.split()]
    if input_nr == N+1:
        new = infected.copy()
        for day in range(D):
            temp = []
            for i in new:
                for h in healthy:
                    if overlap(times[i],times[h]):
                        temp.append(h)

            for t in set(temp):
                infected.append(t)
                healthy.remove(t)
            new = temp.copy()
        print(*sorted(infected))
        break
    input_nr +=1