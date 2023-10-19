nums = list(map(int,input().split()[1:]))
new = nums.copy()
counter = 0
last = nums[-1]
while len(set(new)) > 1:
    temp = []
    for i in range(len(new)-1):
        temp.append(new[i+1]-new[i])
    new = temp.copy()
    counter +=1
    last += new[-1]
print(counter,last)