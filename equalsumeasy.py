from itertools import combinations


def pog(s):
    ans = []
    key = []

    for i in range(1,20):
        for v in combinations(s,i):
            tot = sum(v)
            if tot in ans:
                return(key[ans.index(tot)],v)
            ans.append(tot)
            key.append(v)
    return(0)



t = int(input().strip())
for c in range(t):
    s = tuple(map(int,input().split()[1:]))
    ans = pog(s)
    print(f"Case #{c+1}:")
    if ans == 0:
        print('Impossible')
    else:
        print(*ans[0])
        print(*ans[1])
