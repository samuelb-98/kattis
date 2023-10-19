import sys
innr = 0

def reduce(a,b):
    for i in range(2,int(min(a,b)+1)):
        while a%i == 0 and b%i == 0:
            a//=i
            b//=i
    return([a,b])




for line in sys.stdin:
    if innr == 1:
        line = [int(i) for i in line.split()]
        for i in line[1:]:
            a,b = reduce(i,line[0])
            print(f"{b}/{a}")
        break
    innr +=1