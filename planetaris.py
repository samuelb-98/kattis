n,a = tuple(map(int,input().split()))
pog = list(map(int,input().split()))
pog = sorted(pog)
counter = 0
for i in pog:
    if a-i-1>=0:
        a-=(i+1)
        counter +=1
    else:
        print(counter)
        quit()
print(n)
