n,m = tuple(map(int,input().split()))

counter = 0
pog = [0 for i in range(n)]
for i in range(m):
    a,b = (set(map(int,input().split())))
    if b-a == 1:
        pog[a-1] = i+1
        counter +=1
    elif a-b == 1:
        pog[b-1] = i+1
        counter +=1
    if {a,b} == {1,n}:
        pog[n-1] = i+1
        counter +=1

if counter == n:
    for p in pog:
        print(p)
else:
    print('impossible')