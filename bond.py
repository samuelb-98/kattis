import sys

probs = []
memory = [-1]*(2**20)
completed = [False]*(2**20)

def solve(bond, mask):
    global memory, probs, completed, total_bonds
    if bond == total_bonds:
        return(1.0)
    if completed[mask]:
        return(memory[mask])
    completed[mask] = True
    ans = 0.0
    for i in range(total_bonds):
        if ((mask & (1 << i)) == 0):
            d = probs[bond][i] * solve(bond + 1, mask|(1<<i))
            ans = max(ans, d)

    memory[mask] = ans
    return(ans)
        

input_nr = 0
for line in sys.stdin:
    line = [int(i) for i in line.split()]

    if input_nr == 0:
        total_bonds = line[0]
    else:
        line = [i/100.0 for i in line]
        probs.append(line)


    input_nr += 1
    if input_nr == total_bonds + 1:
        break

print(solve(0,0) * 100)