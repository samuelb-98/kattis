import sys
n = -1
innr = 0
for line in sys.stdin:
    if innr == 0:
        n = int(line.strip())
    if 0 < innr <= n:
        if innr % 2: print(line.strip())
    if innr == n:
        break
    innr +=1
