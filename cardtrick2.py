import sys

for i in range(int(input().strip())):
    x = int(input().strip())

    index = [1]
    for num in range(1,x):
        index.append((sum(index)+num+1)%(x-num))
        print(index)