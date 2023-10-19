

b,d,c,l = [int(i) for i in input().split()]
ans = []

for i in range(l//b+1):
    for j in range(l//d+1):
        for k in range(l//c+1):
            if i*b + j*d + c*k == l:
                ans.append((i,j,k))

if len(ans) == 0:
    print("impossible")
else:
    for a in ans:
        print(*a)