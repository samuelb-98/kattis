from sys import stdin

for line in stdin:
    pog = ""
    s = line.strip()
    for c in s:
        pog += bin(ord(c))[2:].zfill(7)
    
    if not pog.count('1')%2 and not pog.count('0')%2:
        print('free')
    else:
        print('trapped')