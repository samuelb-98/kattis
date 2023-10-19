from sys import stdin


def dist(x1,y1,x2,y2):
    return(((x1-x2)**2 + (y1-y2)**2)**0.5)


for line in stdin:
    d = float(line.split()[0])
    n = int(line.split()[1])
    if not (d or n):
        break
    hives = []
    for i in range(n):
        hives.append(tuple(map(float,input().split())))

    sour = set()
    
    for i in range(n):
        for j in range(n):
            if i == j: continue

            x1,y1 = hives[i]
            x2,y2 = hives[j]

            if dist(x1,y1,x2,y2) <= d:
                sour.add(i)
                sour.add(j)

    print(f"{len(sour)} sour, {n-len(sour)} sweet")