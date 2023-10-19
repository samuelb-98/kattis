while 1:
    n = int(input().strip())
    if not n:
        break
    am = []
    pm = []

    for i in range(n):
        time,bruh = input().split()
        
        h = int(time.split(':')[0])%12
        m = int(time.split(':')[1])


        if bruh == 'a.m.':
            am.append((h,m))
        else:
            pm.append((h,m))

    
        am = sorted(am)
        pm = sorted(pm)


    for h,m in am:
        if h == 0:
            print('12'+':'+str(m).zfill(2)+ ' a.m.')
        else:
            print(str(h)+':'+str(m).zfill(2)+ ' a.m.')

    for h,m in pm:
        if h == 0:
            print('12'+':'+str(m).zfill(2)+ ' p.m.')
        else:
            print(str(h)+':'+str(m).zfill(2)+ ' p.m.')
