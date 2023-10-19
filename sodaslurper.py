e,f,c = [int(i) for i in input().split()]
bottles = e+f
sum = 0
while bottles - c >= 0:
    sum +=1
    bottles -= c - 1
print(sum)