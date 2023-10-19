import sys

birthdays = dict()

input_nr = 0
friends = -1
for line in sys.stdin:
    if input_nr == 0:
        friends = int(line.strip())
    if 0 < input_nr <= friends:
        line = line.split()
        if line[2] in birthdays:
            if int(line[1]) > int(birthdays[line[2]][1]):
                birthdays[line[2]] = line[:2]
        else:
            birthdays[line[2]] = line[:2]
    if input_nr == friends:
        output = []
        for day in birthdays:
            output.append(birthdays[day][0])
        output.sort()
        print(len(output))
        for name in output:
            print(name)
        break
    input_nr +=1