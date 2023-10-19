def dist(a,b):
    return(a**2+b**2)**0.5

pog = [20,40,60,80,100,120,140,160,180,200]

t = int(input().strip())
for c in range(t):
    score = 0
    n = int(input().strip())
    for i in range(n):
        x,y = tuple(map(int,input().split()))
        r = dist(x,y)
        for s in pog:
            if r <= s:
                score += 10 - pog.index(s)
                break
    print(score)