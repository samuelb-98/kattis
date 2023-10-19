from sys import stdin


pog = dict()
for line in stdin:
    if line.strip() == "":
        break

    a,b = line.split()
    pog[b] = a


for line in stdin:
    w = line.strip()
    if w in pog:
        print(pog[w])
    else:
        print('eh')