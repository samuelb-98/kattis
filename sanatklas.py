from math import radians, sin


h,v = tuple(map(int,input().split()))
if v <= 180:
    print("safe")
else:
    print(int(abs(h/sin(radians(v)))))