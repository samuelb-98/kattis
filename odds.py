from sys import stdin

day = 1
for line in stdin:
    if line.strip() == "OPEN":
        pog = dict()
        costs = dict()
    if line.strip() == "CLOSE":
        print("day",day)
        for n,p in sorted(costs.items()):
            print(f"{n} ${p/10}0")
        day+=1
    if line.split()[0] == "ENTER":
        pog[line.split()[1]] = int(line.split()[2])
    if line.split()[0] == "EXIT":
        if line.split()[1] in costs:
            costs[line.split()[1]] += int(line.split()[2]) - pog[line.split()[1]]
        else:
            costs[line.split()[1]] = int(line.split()[2]) - pog[line.split()[1]]