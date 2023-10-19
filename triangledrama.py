import sys


n = -1
innr = 0
for line in sys.stdin:
    if innr == 0:
        n = int(line.strip())
        matrix = []
    if 0 < innr <= n:
        matrix.append([int(i) for i in line.split()])
    if innr == n:
        break
    innr += 1


high = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(i+2,n):
            pog = matrix[i][j] * matrix[j][k] * matrix[i][k]
            if pog > high:
                high = pog
                ans = (i+1,j+1,k+1)

print(*ans)