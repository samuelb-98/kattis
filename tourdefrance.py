import sys

input_nr = 1
for line in sys.stdin:
    line = [int(i) for i in line.split()]

    if input_nr == 1:
        F, R = line
    if input_nr == 2:
        f_teeth = line
    if input_nr == 3:
        r_teeth = line
    if line[0] == 0:
        input_nr = 0

        highest = 0
        ratios = []
        for f_gear in f_teeth:
            for r_gear in r_teeth:
                ratios.append(r_gear/f_gear)

        ratios.sort()
        
        for i in range(F*R-1):
            if highest < ratios[i]/ratios[i+1]:
                highest = ratios[i]/ratios[i+1]
            if highest < 1 / (ratios[i]/ratios[i+1]):
                highest = 1 / (ratios[i]/ratios[i+1])

        print(round(highest,2))
    input_nr += 1