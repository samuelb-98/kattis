import sys
import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom


cases = 0
input_nr = 0
for line in sys.stdin:
    line = [int(i) for i in line.split()]
    if input_nr == 0:
        cases = line[0]
    if 0 < input_nr <= cases:
        P_win = 0
        R, S, X, Y, W = line
        P_one_roll = (S - R + 1) / S
        for x in range(X,Y+1):
            P_win += ncr(Y,x) * P_one_roll**x * (1-P_one_roll)**(Y-x)
        if (W - 1) * P_win > 1 - P_win:
            print("yes")
        else:
            print("no")
        if input_nr == cases:
            break
    input_nr +=1
