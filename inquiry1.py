

from sys import stdin


n = int(input().strip())
nums = []
for i in range(n):
    nums.append(int(stdin.readline()))

left = nums[0]**2
right = sum(nums[1:])
best = 0
for i in range(1,n):
    pog = left*right
    if best < pog:
        best = pog
    shift = nums[i]
    left += shift**2
    right -= shift


print(best)