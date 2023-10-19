s,c,k = tuple(map(int,input().split()))
counter = 1
curr = 0
minc = -1
socks = sorted(tuple(map(int,input().split())))
for i in socks:
    if minc == -1:
        minc = i
    curr +=1
    if curr > c:
        curr = 1
        minc = i
        counter +=1
        continue
    if i - minc > k:
        counter +=1
        minc = i
        curr = 1
        continue


print(counter)