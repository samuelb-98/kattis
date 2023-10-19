x = []
y = []
ans = []
for i in range(3):
    a,b = [int(i) for i in input().split()]
    x.append(a)
    y.append(b)

for a in x:
    if x.count(a) == 1:
        ans.append(a)
for a in y:
    if y.count(a) == 1:
        ans.append(a)
print(*ans)