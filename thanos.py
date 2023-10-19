n = int(input().strip())
for i in range(n):
    p,r,f = tuple(map(int,input().split()))
    counter = 0
    while p <= f:
        counter +=1
        p*=r
        p = int(p)
    print(counter)