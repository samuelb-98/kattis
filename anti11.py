ans = [1,2,3]

def solve(n):
    global ans
    if n < len(ans):
        return(ans[n])
    else:
        k = int((2*solve(n-1) - solve(n-3)) % (1e9+7))
        ans.append(k)
        return(k)

cases = int(input().strip())
while cases > 0:
    print(solve(int(input().strip())))
    cases -=1