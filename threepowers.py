while 1:
    x = int(input().strip())
    if not x: break

    pog = bin(x-1)[2:][::-1]
    ans = []
    for i in range(len(pog)):
        if int(pog[i]):
            ans.append(3**(i))

    out = '{ '
    if len(ans):
        for i in ans[:-1]:
            out+=str(i)+', '
        out+= str(ans[-1])
    out += ' }'
    print(out)