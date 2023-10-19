from sys import stdin


def pog(num):
    ones = ['','one','two','three','four','five','six','seven','eight','nine']
    tens = ['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    bruh = ['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']


    if num == 0:
        return('zero')
    if num < 10:
        return ones[num]
    if 10 < num < 20:
        return bruh[num-11]
    else:
        t = int(str(num)[0])
        o = int(str(num)[1])
        return(tens[t-1]+'-'*int(0<o)+ones[o])

for line in stdin:
    s = line.split()
    out = []
    for w in s:
        try:
            out.append(pog(int(w)))
        except:
            out.append(w)

    if len(out[0]) > 1:
        out[0] = out[0][0].upper() + out[0][1:]
    print(*out)