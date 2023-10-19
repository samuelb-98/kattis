a,b = tuple(map(int,input().split()))
counter = 0
while a != b:
    if a < b:
        counter += b-a
        a = b
    else:
        if a%2:
            a = (a+1)//2
            counter +=2
        else:
            a//=2
            counter +=1
print(counter)