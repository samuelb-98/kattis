n = int(input().strip())
for i in range(n):
    d = int(input().strip())%1000000007
    tot = 8
    for j in range(d-1):
        tot*=9
        if tot > 1000000007:
            tot = tot%1000000007
    print(tot)