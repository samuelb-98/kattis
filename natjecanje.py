n,s,r = list(map(int,input().split()))
dam = sorted(list(map(int,input().split())))
extra = sorted(list(map(int,input().split())))

for i in extra:
    if i in dam:
        continue
    else:
        if i-1 in dam:
            dam.remove(i-1)
        elif i+1 in dam:
            dam.remove(i+1)

print(len(dam))
            
