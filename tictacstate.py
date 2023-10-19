
def solve(x,o):
    for s in x:
        if s in [0,3,6] and s + 1 in x and s + 2 in x:
            return("X wins")
        if s+3 in x and s+6 in x:
            return("X wins")
        if all([i in x for i in [0,4,8]]) or all([i in x for i in [2,4,6]]):
            return("X wins")

    for s in o:
        if s in [0,3,6] and s + 1 in o and s + 2 in o:
            return("O wins")
        if s+3 in o and s+6 in o:
            return("O wins")
        if all([i in o for i in [0,4,8]]) or all([i in o for i in [2,4,6]]):
            return("O wins")

    if len(x) + len(o) == 9:
        return("Cat's")
    else:
        return("In progress")

n = int(input().strip())
for i in range(n):
    num = bin(int(input().strip(),8))[2:].zfill(18)
    x = set()
    o = set()    
    for s in range(1,10):
        if int(num[-s]):
            if int(num[-9-s]):
                x.add(s-1)
            else:
                o.add(s-1)

    print(solve(x,o))