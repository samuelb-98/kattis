


def move(board,i,dir):
    new = board.copy()
    new[i] = '-'
    new[i+dir] = '-'
    new[i+2*dir] = 'o'
    return(new)

def solve(board,depth):
    global deepest 
    if depth > deepest:
        deepest = depth
    right = []
    left = []
    for i in range(10):
        if board[i] == "o" and board[i+1] == "o" and board[i+2] == "-":
            right.append(i)

    for i in range(1,11):
        if board[-i] == "o" and board[-i-1] == "o" and board[-i-2] == "-":
            left.append(12-i)

    for p in right:
        solve(move(board,p,1),depth+1)
    for p in left:
        solve(move(board,p,-1),depth+1)

    return


n = int(input().strip())
for i in range(n):
    deepest = 0
    board = list(input().strip())
    start = board.count('o')
    solve(board,0)
    print(start-deepest)