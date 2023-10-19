n,v = tuple(map(int,input().split()))
best = -v
for i in range(n):
    a,b,c = tuple(map(int,input().split()))
    pog = (a*b*c)-v
    if pog > best:
        best = pog
    
print(best)