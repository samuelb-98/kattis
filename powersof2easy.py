n,e = list(map(int,input().split()))
pog = str(2**e)
counter = 0
for i in range(n+1):
    if pog in str(i):
        counter +=1

print(counter)