from math import ceil


n = int(input().strip())
for i in range(n):
    s = input().strip()
    key = ""
    for c in s:
        key += c
        x = 1
        while s[(x-1)*len(key):x*len(key)] == key:
            print(s[(x-1)*len(key):x*len(key)])
            x +=1
        if x == len(s)/len(key):
            print(len(key), key)
            break