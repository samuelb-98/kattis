import sys
up = 0
down = 0
N = -1
input_nr = 0
for line in sys.stdin:
    if input_nr == 0:
        N = int(line.strip())
        sum = 7
    if 0 < input_nr <= N:
        if line.strip() == "Skru op!":
            if sum < 10:
                sum +=1
        else:
            if sum > 0:
                sum -=1
    if input_nr == N:
        print(sum)
        break
    input_nr +=1