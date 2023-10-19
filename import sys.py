import sys
innr = 0
N = -1
nrs = []
for line in sys.stdin:
    if innr == 0:
        N = int(line.strip())
    if 0 < innr <= N:
        nrs.append(int(line.strip()))
    if innr == N:
        print(nrs*)