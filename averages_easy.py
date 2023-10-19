import sys

input_nr = 0
for line in sys.stdin:
    line = [int(i) for i in line.split()]

    if input_nr == 0:
        test_cases = line[0]

    if 1 < input_nr <= 4*test_cases + 1:
        if input_nr % 4 == 2:
            NCS, NE = line
        if input_nr % 4 == 3:
            sciq = line
        if input_nr % 4 == 0:
            eiq = line

           
            csavg = sum(sciq)/NCS
            eavg = sum(eiq)/NE
            counter = 0
            for student in sciq:
                if eavg < student < csavg:
                    counter += 1
            print(counter)
    
    if input_nr == 4*test_cases:
        break
    input_nr += 1


