import sys

R, C = 0, 0
cords = []
input_nr = 0
for line in sys.stdin:
    if input_nr == 0:
        R, C = [int(i) for i in line.split()]
        visited = []
        for i in range(R):
            bruh = []
            for i in range(C):
                bruh.append(0)
            visited.append(bruh)
    if 0 < input_nr <= R:
        line = line.strip()
        cords.append(line)
    if input_nr == R:
        curr = [0, 0]
        step = 0
        while True:
            if 0 > curr[0] or 0 > curr[1] or R <= curr[0] or C <= curr[1]:
                print("Out")
                break
            if cords[curr[0]][curr[1]] == "T":
                print(step)
                break
            if visited[curr[0]][curr[1]] == 1:
                print("Lost")
                break
            else:
                visited[curr[0]][curr[1]] = 1
            pos = cords[curr[0]][curr[1]]
            if pos == "N":
                curr[0] -=1
            if pos == "S":
                curr[0] +=1
            if pos == "W":
                curr[1] -=1
            if pos == "E":
                curr[1] +=1
            step +=1

        break
    input_nr +=1