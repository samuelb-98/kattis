t = int(input().strip())
for c in range(t):
    l,n = tuple(map(int,input().split()))
    ants = []
    counter = 0
    while counter < n:
        for a in tuple(map(int,input().split())):
            ants.append(a)
            counter += 1

    minlast = 0
    maxdist = 0

    for ant in ants:
        right = l - ant
        left = ant

        if minlast < min(left,right):
            minlast = min(left,right)
        
        if maxdist < max(left,right):
            maxdist = max(left,right)
        
    
    print(minlast,maxdist)