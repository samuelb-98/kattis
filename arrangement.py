import sys
nr = 0
for line in sys.stdin:
    if nr == 0:
        N = int(line.strip())
    if nr == 1:
        M = int(line.strip())

        for i in range(N - M%N):
            print("*"*(M//N))

        for i in range(M%N):
            print("*"*(M//N+1))
        break
    nr +=1

 