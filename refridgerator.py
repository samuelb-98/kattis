from math import ceil


pa,ka,pb,kb,n = tuple(map(int,input().split()))

maxa = ceil(n/ka)
best = (0,0,100000)
for i in range(maxa+1):

    j = ceil((n-i*ka)/kb)

    cost = i*pa + j*pb
    if cost < best[2]:
        best = (i,j,cost)  

print(*best)