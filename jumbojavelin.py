import sys

n = -1
innr = 0
for line in sys.stdin:
    if innr == 0:
        n = int(line.strip())
        s = 0
    if 0 < innr <= n:
        s += int(line.strip()) - 1
    if innr == n:
        print(s+1)
        break
    innr += 1