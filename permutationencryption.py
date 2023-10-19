while 1:
    pog = list(map(int,input().split()))
    key = pog[1:]
    l = pog[0]
    if l == 0:
        break
    s = input().strip()
    s += ' '*((l-len(s)%l)%l)
    out = ""
    for i in range(len(s)//l):
        w = s[l*i:l*(i+1)]
        for j in key:
            out += w[j-1]
    print("'" + out + "'")