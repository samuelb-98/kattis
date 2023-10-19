n = int(input().strip())
peaks = [int(i) for i in input().split()]


hr = 0
hl = 0
low = 0
best = 0

for h in peaks:
    if h >= hl:
        if best < hl - low:
            best = hl - low
        low = h        
        hl = h

    if h < low:
        low = h
        hr = h

    if h > hr:
        hr = h

    if hr - low > best:
        best = hr - low

print(best)
