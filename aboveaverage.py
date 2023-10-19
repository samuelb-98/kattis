import sys
cases = -1
nr = 0
for line in sys.stdin:
    line = [int(i) for i in line.split()]
    if nr == 0:
        cases = line[0]
    if 0 < nr <= cases:
        counter = 0
        grades = line[1:]
        avg = sum(grades)/len(grades)
        for i in grades:
            if avg < i:
                counter +=1

        print('{:.3f}%'.format(round(counter/len(grades)*100, 3)))
        #print(str(round(counter/len(grades)*100,3))+"%")

    if nr == cases:
        break
    nr += 1