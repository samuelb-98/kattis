import sys

for line in sys.stdin:
    if line.strip() == "0 0":
        break
    line = line.split()
    while len(line[0]) < len(line[1]):
        line[0] = "0" + line[0]
    while len(line[1]) < len(line[0]):
        line[1] = "0" + line[1]
    counter = 0
    prev = False
    for i in range(1,min(len(line[0]),len(line[1]))+1):
        if prev == False:
            if int(line[0][-i]) + int(line[1][-i]) >= 10:
                counter +=1
                prev = True
            else:
                prev = False
        else:
            if int(line[0][-i]) + int(line[1][-i]) >= 9:
                counter +=1
                prev = True
            else:
                prev = False
    if counter == 0:
        print("No carry operation.")
    if counter == 1:
        print("1 carry operation.")
    if 1 < counter:
        print(f"{counter} carry operations.")

