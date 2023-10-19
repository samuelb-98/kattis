x = int(input().strip())
y = int(input().strip())

if x < 0:
    if y < 0:
        print(3)
    else:
        print(2)
else:
    if y < 0:
        print(4)
    else:
        print(1)