n,m = tuple(map(int,input().split()))
grid = [list('.'*(m+2))]
for i in range(n):
    grid.append(list('.' + input().strip() + '.'))
grid.append(list('.'*(m+2)))



while 1:
    old = []
    [old.append(row.copy()) for row in grid]

    for row in range(1,n+1):
        for col in range(1,m+1):
            if grid[row][col] == 'V':
                if grid[row+1][col] in '.V':
                    grid[row+1][col] = 'V'
                else:
                    if grid[row][col+1] != '#':
                        grid[row][col+1] = 'V'
                    if grid[row][col-1] != '#':
                        grid[row][col-1] = 'V'
    


    if grid == old:
        break

for row in range(1,n+1):
    print("".join(grid[row][1:-1]))