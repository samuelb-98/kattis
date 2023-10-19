import sys

for n in sys.stdin:
    i = 0
    k = 0

    while i <= int(n) :
        i += (1+2*k)**2
        k+=1
    print(k-1)