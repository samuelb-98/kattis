

def solve(towns):
    ans = []
    for town in towns:
        town = sorted(town)[::-1]
        l = len(town)
        i = 0
        while 0 < l and i < len(town):
            l -= town[i]
            i+=1

        if l < 1:
            ans.append(i)
        else:
            return(0)
    return(ans)


cases = int(input().strip())
for case in range(cases):
    n,t = tuple(map(int,input().split()))
    e = int(input().strip())
    towns = [[] for i in range(n)]
    for i in range(e):
        h,p = tuple(map(int,input().split()))
        if h == t: continue
        towns[h-1].append(p)
    

    ans = solve(towns)
    if not ans:
        print(f"Case #{case+1}: IMPOSSIBLE")
    else:
        print(f"Case #{case+1}:", *ans)

        
    