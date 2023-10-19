n = int(input().strip())
nodes = [0 for i in range(n)]
for i in range(n-1):
    a,b,x,t = tuple(map(int,input().split()))
    nodes[b-1] = (a,x/100,t)

needed = list(map(int,input().split()))
water = [(1,0)]

for node in range(2,n+1):
    source,frac,t = nodes[node-1]
    w,squares = water[source-1]
    w = (w*frac)**(1+t)
    squares += t
    water.append((w,squares))
ans = []
for i in range(n):
    if needed[i] == -1: continue
    else:
        ans.append((needed[i]/water[i][0])**(1/(2**water[i][1])))

print(max(ans))