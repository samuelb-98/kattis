import sys
INF = 1000000
innr = 0
L = -1
for line in sys.stdin:
    line = [int(i) for i in line.split()]

    if innr == 0:
        N,H,L = line
        similar = [[] for i in range(N)]
    if innr == 1:
        horrors = line
    if 1 < innr <= L+1:
        similar[line[0]].append(line[1])
        similar[line[1]].append(line[0])
    if innr == L+1:
        break
    innr +=1



q = []
not_visited = set(range(N))
for h in horrors:
    not_visited.remove(h)
    q.append((0,h))
c,i = -1,-1
while len(q)>0:
    cost, v = q.pop(0)
    if cost > c or (cost == c and v < i):
        c,i = cost, v
    for u in similar[v]:
        if u in not_visited:
            not_visited.remove(u)
            q.append((cost+1,u))
if not not_visited:
    print(i,)
else:
    print(min(not_visited))

