n = int(input().strip())
for i in range(n):
    num = list(input().split()[1])
    out = [i+1]
    for base in [8,10,16]:
        ans = 0
        for v,d in enumerate(num[::-1]):
            if base == 8 and d in '89':
                ans = 0
                break
            ans+= int(d)*base**v
        out.append(ans)
    print(*out)