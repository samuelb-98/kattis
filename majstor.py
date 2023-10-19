

def pog(a,b):
    bruh = "RPS"
    x = bruh.index(a)
    y = bruh.index(b)
    if (y-x)%3 == 1:
        return 0
    elif (y-x)%3 == 2:
        return 2
    else:
        return 1


r = int(input().strip())
sven = input().strip()
f = int(input().strip())
friends = []
for i in range(f):
    friends.append(input().strip())

score = 0
best = 0
for i in range(r):
    bruh = 0
    for c in 'RPS':
        new = 0
        for j in friends:
            score+=pog(sven[i],j[i])
            new += pog(c,j[i])
        if bruh < new:
            bruh = new
    best += bruh

print(score//3)
print(best)

