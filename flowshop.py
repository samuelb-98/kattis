n,m = tuple(map(int,input().split()))
mac = []
for i in range(n):
    mac.append(list(map(int,input().split())))


for i in range(1,n):
    mac[i][0] += mac[i-1][0]

for i in range(1,m):
    mac[0][i] += mac[0][i-1]

for i in range(1,n):
    for j in range(1,m):
        mac[i][j] += max(mac[i][j-1],mac[i-1][j])
    
ans = []
for i in range(n):
    ans.append(mac[i][-1])

print(*ans)