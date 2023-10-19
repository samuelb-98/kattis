t = int(input().strip())
for c in range(t):
    dig = [0 for i in range(10)]
    a = input().strip()
    b,c = input().split()
    b = int(b)
    nums = []
    while len(nums) < b:
        line = input().split()
        if line[0] == "+":
            for i in range((int(line[2])-int(line[1]))//int(line[3])+1):
                nums.append(int(line[1])+i*int(line[3]))
        else:
            nums.append(int(line[0]))

    for n in nums:
        for d in str(n):
            dig[int(d)] += 1
    
    print(a)
    print(b,c)

    for i in range(10):
        print("Make", dig[i], "digit", i)
    
    print("In total", sum(dig), "digit" + (sum(dig)!=1)*'s')