from sys import stdin

pog = dict()
for line in stdin:
    line = line.split()
    if line == ['0']:
        break
    if len(line) < 3:
        print(*line)
    else:    
        nums = 0
        vars = []
        if line[1] == '=':
            if line[2] in pog:
                pog[line[0]] = pog[line[2]]
            else:
                pog[line[0]] = int(line[2])
        else:
            for x in line:
                if x == '+': continue
                try:
                    nums += int(x)
                except:
                    if x in pog:
                        nums += pog[x]
                    else:
                        vars.append(x)
            if nums != 0:
                print(str(nums),*vars,sep=' + ')
            else:
                print(*vars,sep=' + ')