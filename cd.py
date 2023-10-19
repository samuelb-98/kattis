import sys

jack = []
jill = []


def bin_ser(list,goal):
    lo = 0
    hi = len(list)-1
    curr = (lo + hi)//2
    while list[curr] != goal:
        curr = (lo + hi)//2
        if list[curr] < goal and list[curr+1] > goal:
            return(0,curr)
        if list[curr] < goal:
            lo = curr
        else:
            hi = curr
    return(1,curr)



innr = 0
for line in sys.stdin:
    if line.strip() == "0 0":
        break
    if innr == 0:
        M,N = [int(i) for i in line.split()]
    if 0 < innr <= M:
        jack.append(int(line.strip()))
    if M < innr <= M+N:
        jill.append(int(line.strip()))
    if innr == N+M:
        counter = 0
        if len(jack) < len(jill):
            for cd in jill:
                temp
                counter += bin_ser(jack, cd)
        else:
            for cd in jack:
                counter += bin_ser(jill,cd)
        print(counter)
    innr +=1