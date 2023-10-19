


from collections import deque


def isprime(n):
    if n in [0,1]:
        return False
    elif n in [2,3,5,7]:
        return True
    else:
        for i in range(2,int(n**0.5)+1):
            if not n%i:
                return False
        return True
     
def FN(x):
    ints = list(str(x))
    nei = set()
    for i in range(4):
        temp = ints.copy()
        for j in range(10):
            if not i and not j: continue
            temp[i] = str(j)
            new = int("".join(temp))
            if isprime(new):
                nei.add(new)
    return(nei)


def BFS(start,goal):

    visited = set()
    q = deque()
    q.append((start,0))
    visited.add(start)
    while len(q):
        curr,dist = q.popleft()
        if curr == goal:
            return(dist)
        
        for nei in FN(curr):
            if nei not in visited:
                q.append((nei,dist+1))
                visited.add(nei)
        
    return('Impossible')



t = int(input().strip())
for c in range(t):
    start,goal = [int(i) for i in input().split()]

    print(BFS(start,goal))
    
