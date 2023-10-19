n = int(input().strip())
ing = []
for i in range(n):
    ing.append(tuple(map(int,input().split())))

best = 1000000

for i in range(1,2**n):

    key = list(map(int,bin(i)[2:][::-1]))
    s = 1
    b = 0
    for i,k in enumerate(key):
        if k:
            s*=ing[i][0]
            b+=ing[i][1]


    if abs(s-b) < best:
        best = abs(s-b)

print(best)