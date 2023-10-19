c = int(input().strip())
comps = [[] for i in range(c)]
s = [0 for i in range(c)]
tdays = set()
for i in range(c):
    days = int(input().strip())
    for d in range(days):
        n,d = tuple(map(int,input().split()))
        comps[i].append((n,d))
        tdays.add(d)

tdays = sorted(list(tdays))
ans = []
for day in range(1,366):
    for i,com in enumerate(comps):
        for x,d in com:
            if d == day:
                s[i] = x
    if day in tdays:
        ans.append(sum(s))
    
print(*ans)