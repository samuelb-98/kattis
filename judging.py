import sys

results1 = dict()
results2 = dict()
all_ans = set()
N = 0
input_nr = 0
for line in sys.stdin:
    line = line.strip()
    if input_nr == 0:
        N = int(line)


    if 0 < input_nr <= N:
        all_ans.add(line)
        if line in results1:
            results1[line] +=1
        else:
            results1[line] = 1

    if N < input_nr <= 2*N:
        all_ans.add(line)
        if line in results2:
            results2[line] +=1
        else:
            results2[line] = 1

    
    if input_nr == 2*N:
        counter = 0
        for ans in all_ans:
            if ans in results1 and ans in results2:
                counter += min(results1[ans],results2[ans])
        print(counter)



    input_nr +=1