def dist(x1,y1,x2,y2):
    return(((x1-x2)**2+(y1-y2)**2)**0.5)


def solve(x,y,candles):
    for x1,y1 in candles:
        if dist(x,y,x1,y1) <= 8:
            return("light a candle")
    return("curse the darkness")

t = int(input().strip())
for c in range(t):
    x,y = tuple(map(float,input().split()))
    n = int(input().strip())
    candles = []
    for i in range(n):
        candles.append(tuple(map(float,input().split())))
    print(solve(x,y,candles))
            