import sys
R = -1
innr = 0
for line in sys.stdin:
    if innr == 0:
        R,C,Zr,Zc = [int(i) for i in line.split()]
    if 0 <  innr <= R:
        new = ""
        line = line.strip()
        for char in line:
            new += char * Zc
        for i in range(Zr):
            print(new)
    innr +=1