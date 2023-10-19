from sys import stdin
from collections import Counter

names = []
for line in stdin:
    names.append(line.split())
names = sorted(names,key=lambda x:(x[1],x[0]))

counter = Counter(x[0] for x in names)

for f,l in names:
    if counter[f] == 1:
        print(f)
    else:
        print(f,l)