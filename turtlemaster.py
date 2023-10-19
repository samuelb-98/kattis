import sys

def tmove(tr,tc,to):
    to = to%4
    if to == 0:
        tc += 1
    elif to == 1:
        tr -= 1
    elif to == 2:
        tc -= 1
    else: tr +=1
    return(tr,tc,to)


board = [[] for i in range(8)]

for row in range(8):
    for tile in input().strip():
        board[row].append(tile)

commands = input().strip()

tr = 7
tc = 0
to = 0

for c in commands:
    if c == 'F':
        tr,tc,to = tmove(tr,tc,to)
        if board[tr][tc] in ['C', 'I']:
            print("Bug!")
            quit()
        if not (0<=tr<=7 and  0<=tc<=7):
            print("Bug!")
            quit()

    elif c == 'R':
        to -=1
    elif c == 'L':
        to += 1
    else:
        r,c,o = tmove(tr,tc,to)
        if board[r][c] != 'I':
            print("Bug!")
            quit()
        else:
            board[r][c] = '.'


if board[tr][tc] == 'D':
    print("Diamond!")
else:
    print("Bug!")