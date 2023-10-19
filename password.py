n = int(input().strip())
pog = []
for i in range(n):
    pog.append(float(input().split()[1]))

tot = 0
for i,v in enumerate(sorted(pog)[::-1]):
    tot += (i+1)*v

print(tot)