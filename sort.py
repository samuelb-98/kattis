n,c = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]

freq = dict()
counter = c

for i in nums:
    if i in freq:
        freq[i][0] +=1
    else:
        freq[i] = [1,counter]
        counter -=1

pog = sorted(freq.items(),key= lambda x:x[1])[::-1]
out = []
for i in pog:
    for j in range(i[1][0]):
        out.append(i[0])
print(*out)