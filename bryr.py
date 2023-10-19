
from collections import deque


def solve(start,goal,adj):
    q = deque()
    pog = set()
    w = [-1 for i in range(goal)]
    w[0] = 0
    q.append((start,0))
    while len(q):
        curr,cost = q.popleft()
        if curr == goal:
            pog.add(cost)
        for nei,wei in adj[curr-1]:
            if w[nei-1] == -1 or w[nei-1] > cost+wei:
                w[nei-1] = cost+wei
                q.append((nei,cost+wei))
    return(min(pog))

n,m = tuple(map(int,input().split()))
adj = [[] for i in range(n)]
for i in range(m):
    a,b,w = tuple(map(int,input().split()))
    adj[a-1].append((b,w))
    adj[b-1].append((a,w))
print(solve(1,n,adj))