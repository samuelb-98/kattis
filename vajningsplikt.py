key = ['North','East','South','West']
a,b,c = input().split()

a = key.index(a)
b = key.index(b)
c = key.index(c)

pog = False

if b == (a+2)%4:
    if c == (a-1)%4:
        pog = True

if b == (a+1)%4:
    if c == (a+2)%4 or c == (a-1)%4:
        pog = True


if pog:
    print("Yes")
else:
    print("No")