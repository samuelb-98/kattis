import bisect

extra = 0

l,d,n = [int(i) for i in input().split()]
l-=12
pos = []
for i in range(n):
    bisect.insort(pos,int(input())-6)


if n == 0:
    print(l//d + 1)

else:

    extra += pos[0]//d
    extra += (l-pos[-1])//d

    if n > 1:
        for i in range(len(pos)-1):
            extra += (pos[i+1]-pos[i])//(d) - 1

    print(extra)