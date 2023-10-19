from sys import stdin

def dist(x1,y1,x2,y2):
    return(((x1-x2)**2+(y1-y2)**2)**0.5)

def solve(xg,yg,xd,yd,holes):
    for xh,yh in holes:
        x = "{:.3f}".format(xh)
        y = "{:.3f}".format(yh)
        if 2*dist(xg,yg,xh,yh) <= dist(xd,yd,xh,yh):
            return(f"The gopher can escape through the hole at ({x},{y}).")
    return("The gopher cannot escape.")

xg,yg,xd,yd = tuple(map(float,input().split()))
holes = []
for line in stdin:
    if line.strip() == '0':
        break
    x,y = tuple(map(float,line.split()))
    holes.append((x,y))

print(solve(xg,yg,xd,yd,holes))
