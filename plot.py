nums = list(map(int,input().split()[1:]))[::-1]
n = len(nums)
print(nums)
for i in range(n):
    pog = 0
    prev = 0
    for p,c in enumerate(nums):
        pog += c*i**p
    print(pog-prev)
    prev = pog