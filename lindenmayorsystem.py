n,m = tuple(map(int,input().split()))
rules = dict()
for i in range(n):
    x,dump,y = input().split()
    rules[x] = y
s = input().strip()

for i in range(m):
    new = ""
    for c in s:
        if c in rules:
            new += rules[c]
        else:
            new+=c
    s = new
    
print(s)