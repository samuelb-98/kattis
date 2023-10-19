
from collections import deque


def bfs(start,roads):
    q = deque()
    visited = set()
    q.append(start)
    visited.add(start)
    while len(q):
        curr = q.popleft()
        for nei in roads[curr]:
            if nei not in visited:
                q.append(nei)
                visited.add(nei)
    return visited


t = int(input().strip())
for c in range(t):
    n = int(input().strip())
    roads = [set() for i in range(n)]
    m = int(input().strip())
    for i in range(m):
        a,b = list(map(int,input().split()))
        roads[a].add(b)
        roads[b].add(a)

    counter = -1
    found = [False for i in range(n)]
    for i in range(n):
        if found[i]:continue
        for f in bfs(i,roads):
            found[f] = True
        counter +=1
    print(counter)