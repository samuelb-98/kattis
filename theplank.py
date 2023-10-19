import math

n = int(input().strip())

ans = []
tot = 0

for i in range(n+1):
    for j in range(n+3//2):
        for k in range(n+4//3):
            if i + 2*j + 3*k == n:
                ans.append((i,j,k))

for pog in ans:
    bruh = math.factorial(sum(pog))
    for i in pog:
        bruh /= math.factorial(i)
    tot += bruh
print(int(tot))

    