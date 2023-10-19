import sys

innr = 0
for line in sys.stdin:
    if line.strip() == "-1":
        break
    if innr == 0:
        m = int(line.strip())
        speeds = []
        times = [0]
        total = 0
    if 0 < innr <= m:
        speeds.append([int(i) for i in line.split()][0])
        times.append([int(i) for i in line.split()][1])
    if innr == m:
        for i in range(m):
            total += speeds[i] * (times[i+1]-times[i])
        print(total,"miles")
        innr = -1
    innr +=1