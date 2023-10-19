import sys


def dist(a,b):
    return(((b[0]-a[0])**2 + (b[1]-a[1])**2)**0.5)


cases = 0
input_nr = 0
H = -10
S = -10
for line in sys.stdin:
    line = [int(i) for i in line.split()]
    if input_nr == 0:
        cases = line
    if input_nr == 1:
        S, H = line
        hatches = []
    if 1 < input_nr <= H+1:
        hatches.append(line)
    if input_nr == H+1:
        solutions = []
        for x in range(S+1):
            for y in range(S+1):
                max_leash = min(x,y,S-x,S-y)
                longest = 0
                for hatch in hatches:
                    if longest < dist(hatch, [x,y]):
                        longest = dist(hatch, [x,y])
                if longest <= max_leash and [x,y] not in hatches:
                    solutions.append([x,y])
        
        if len(solutions) == 0:
            print("poodle")
        else:
            print(solutions[0][0],solutions[0][1])
        input_nr = 0
    input_nr +=1