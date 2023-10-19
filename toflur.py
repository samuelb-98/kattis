n = int(input().strip())
nums = sorted(list(map(int,input().split())))
tot = 0
for i in range(n-1):
    tot += (nums[i] - nums[i+1])**2
print(tot)