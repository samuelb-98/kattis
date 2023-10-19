from math import ceil


def dist(x1,y1,x2,y2):
    return(((x1-x2)**2+(y1-y2)**2)**0.5)


dists = []
x,y,n = tuple(map(int,input().split()))
for i in range(n):
    x1,y1,r = tuple(map(int,input().split()))
    dists.append(dist(x,y,x1,y1)-r)

print(max(0,int(sorted(dists)[2])))