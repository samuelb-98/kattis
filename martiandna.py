import re
import sys


def find_shortest(seq,req):
    lo = 0
    minss = 0
    for i in req:
        minss += int(req[i][0])
    hi = minss
    best = len(seq)
    for i in seq[lo:hi]:
        if i in req:
            req[i][1] +=1
    
    for lo in range(len(seq)-minss):
        if seq[lo] not in req:
            continue
        else:
            while hi-lo < best and not complete(reqs) and hi < len(seq):
                print(seq[lo:hi])
                while seq[hi] not in reqs or hi == len(seq):
                    hi +=1
                reqs[seq[hi]][1] +=1
                hi +=1
            
            if complete(reqs):
                if hi-lo < best:
                    best = hi-lo
            reqs[seq[lo]][1] -=1

    return(best)
                
def complete(reqs):
    for i in reqs:
        if reqs[i][1] < int(reqs[i][0]):
            return(False)
    return(True)
    



reqs = dict()
R = -1
input_nr = 0
for line in sys.stdin:
    line = line.split()
    if input_nr == 0:
        N,K,R = [int(i) for i in line]
    if input_nr == 1:
        dna = line
    if 1 < input_nr <= R+1:
        reqs[line[0]] = [line[1], 0]
    if input_nr == R+1:
        print(find_shortest(dna,reqs))

        break
    input_nr +=1