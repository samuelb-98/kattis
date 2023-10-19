import sys

input_nr = 0
modnumbers = []
for line in sys.stdin:
    line = int(line.strip())
    line = line % 42
    if line not in modnumbers:
        modnumbers.append(line)
    input_nr += 1
    if input_nr == 10:
        print(len(modnumbers))
        break
