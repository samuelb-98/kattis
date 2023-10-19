a = list(map(int,input().split(':')))
b = list(map(int,input().split(':')))

if a == b:
    print('24:00:00')
else:
    s = b[2]-a[2]
    m = b[1]-a[1] + s//60
    h = b[0]-a[0] + m//60


    print(f"{(str(h%24).zfill(2))}:{(str(m%60).zfill(2))}:{(str(s%60).zfill(2))}")