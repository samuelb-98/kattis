from math import ceil
from sys import stdin


n = int(input().strip())
nums = tuple(map(int,stdin.readline().split()))
tot = sum(nums)
run = 0
i = 0
if tot%3:
    print(-1)
else:
    ans = []
    while i<n:
        run += nums[i]
        if run == tot//3:
            ans.append(i+1)
            run = 0
        i +=1
    if len(ans) == 3:
        print(*ans[:-1])
    else:
        print(-1)
            