
from collections import deque


def bfs(start,pog):
    q = deque()
    q.append(start)
    visited = set()
    visited.add(start)
    while len(q):
        curr = q.popleft()
        if curr in pog:
            for nei in pog[curr]:
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)
    return visited


def solve(x,y,pog):
    if len(x) != len(y):
        return "no"

    for i,c in enumerate(x):
        if c in pog:
            if y[i] not in pog[c]:
                return("no")
        else:
            if c != y[i]:
                return("no")
    return("yes")


                
a,b = tuple(map(int,input().split()))
pog = dict()
for i in range(a):
    x,y = input().split()
    if x in pog:
        pog[x].add(y)
    else:
        pog[x] = set([y])
for i in pog:
    pog[i] = bfs(i,pog)


for i in range(b):
    x,y = input().split()
    print(solve(x,y,pog))
