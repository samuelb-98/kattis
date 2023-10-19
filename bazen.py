line_start = [int(i) for i in input().split()]
total_area = 250*250/2


def find_area(a,b,c):
    area = 1/2 * (a[0]*(b[1]-c[1])+b[0]*(c[1]-a[1])+c[0]*(a[1]-b[1]))
    return(abs(area))

if sum[line_start] == 250:
    if line_start[0] < 125:
        pass
    else:
        pass

if line_start[0] == 0:
    if line_start[1] < 125:
        pass
    else:
        pass

if line_start[1] == 0:
    if line_start[0] < 125:
        pass
    else:
        pass

print(find_area([0,0],[0,1],[1,0]))