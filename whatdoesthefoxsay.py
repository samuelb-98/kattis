from sys import stdin


t = int(input().strip())
for c in range(t):
    s = input().split()
    pog = set()
    for line in stdin:
        if line.strip() ==  "what does the fox say?":
            break
        else:
            pog.add(line.split()[2])
    ans = []
    for w in s:
        if w not in pog:
            ans.append(w)
    print(*ans)