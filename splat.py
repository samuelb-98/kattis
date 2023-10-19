from cmath import pi


def dist(x1,y1,x2,y2):
    return(((x1-x2)**2+(y1-y2)**2)**0.5)

def pog(px,py,drops):
    for x,y,r,col in drops[::-1]:
        if dist(px,py,x,y) <= r:
            return col
    return("white")


t = int(input().strip())
for c in range(t):
    splats = int(input().strip())
    drops = []
    for d in range(splats):
        x,y,v,col = input().split()
        r = (float(v)/pi)**0.5
        drops.append((float(x),float(y),r,col))
    
    nrpoints = int(input().strip())
    ans = []
    for p in range(nrpoints):
        px,py = tuple(map(float,input().split()))
        ans.append(pog(px,py,drops))

    [print(x) for x in ans]