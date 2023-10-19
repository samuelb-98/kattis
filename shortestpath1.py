import sys
import heapq

def find_shortest_distance(source,edges):
    INF = 10000000
    N = len(edges)
    visited = [False for i in range(N)]
    dists = [INF for i in range(N)]
    dists[source] = 0
    visited[source] = True
    q = [(0,source)]
    while len(q) > 0:
        d,p = heapq.heappop(q)
        for next in edges[p]:
            if d+next[0] < dists[next[1]]:
                heapq.heappush(q,(d+next[0],next[1]))
                visited[next[1]] = True
                dists[next[1]] = d + next[0]
    return dists
    

m = -1
innr = 0
for line in sys.stdin:
    if line.strip() == "0 0 0 0":
        break

    if innr == 0:
        n,m,q,s = [int(i) for i in line.split()]
        edges = [[] for i in range(n)]
        
    if 0 < innr <= m:
        p1,p2,w = [int(i) for i in line.split()]
        edges[p1].append((w,p2))
    if  innr == m:
        dists = find_shortest_distance(s,edges)

    if m < innr <= m+q:
        target = int(line.strip())
        if dists[target] == 10000000:
            print("Impossible")
        else:
            print(dists[target])
        
    if innr == m+q:
        innr = -1
    innr +=1