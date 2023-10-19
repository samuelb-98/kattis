i = int(input())

def find_lenght(M):
    sum = 0
    lenght = 1
    while sum + 2**((lenght-1)//2) < M:
        sum += 2**((lenght-1)//2)
        lenght += 1
    return(lenght,M-sum-1)


lenght, number = find_lenght(i)

if lenght <= 2:
    print([1,3][i-1])
else:
    if lenght % 2 == 0:
        print(int(("1" + format(number, "0" + str(lenght//2-1) + "b") + format(number, "0" + str(lenght//2-1) + "b")[::-1] + "1"),2))
    else:
        print(int(("1" + format(number, "0" + str(lenght//2) + "b") + format(number, "0" + str(lenght//2) + "b")[::-1][1:] + "1"),2))

