t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    v1 = list(map(int,input().split()))
    v2 = list(map(int,input().split()))

    v1 = sorted(v1)
    v2 = sorted(v2)[::-1]
    tot = 0
    for x in range(n):
        tot += v1[x]*v2[x]
    
    print(f"Case #{i+1}:",tot)