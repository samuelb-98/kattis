t = int(input().strip())
for c in range(t):
    s,d = [int(i) for i in input().split()]
    x = (s+d)//2
    y = s-x
    if x+y == s and x-y == d:
        print(x,y)
    else:
        print("impossible")