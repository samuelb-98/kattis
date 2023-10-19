import sys
input_nr = 0
for line in sys.stdin:
    if input_nr == 0:
        line = [int(i) for i in line.split()]
        bruh = sorted(line)
    if input_nr == 1:
        out = []
        for char in line.strip():
            if char == "A":
                out.append(bruh[0])
            if char == "B":
                out.append(bruh[1])
            if char == "C":
                out.append(bruh[2])
        print(*out)
    input_nr +=1

