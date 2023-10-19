

t = int(input().strip())
for i in range(t):
    best = 0
    number = input().strip()
    curr = ""
    for d in number:
        curr += d
        count = bin(int(curr))[2:].count('1')
        if count > best:
            best = count
        
    print(best)