a,b,c = list(map(int,input().split()))
d1 = b-a
d2 = c-b

if d1 == d2:
    print("cruised")
elif d1*d2 > 0:
    if abs(d2) < abs(d1):
        print("braked")
    else:
        print("accelerated")
else:
    print("turned")