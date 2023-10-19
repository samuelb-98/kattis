
from collections import deque


def bfs(start,goal,adj):
    q = deque()
    best = [-1 for i in range(len(adj))]
    q.append((start,0))
    best[start] = 0
    while len(q):
        curr,d = q.popleft()
        for nei,cost in enumerate(adj[curr]):
            if nei == curr: continue
            if best[nei] == -1 or d+cost < best[nei]:
                q.append((nei,d+cost))
                best[nei] = d+cost
    return(best[goal])

n,s,t = tuple(map(int,input().split()))
adj = [[] for i in range(n)]
for i in range(n):
    adj[i] = list(map(int,input().split()))
print(bfs(s,t,adj))