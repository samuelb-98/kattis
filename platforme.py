
def length(platforms):
    pillar_lenght =0
    for i,(y,x1,x2) in enumerate(platforms):
        left,right = -1,-1
        x2-=1
        for y2,x3,x4 in reversed(platforms[:i]):
            x4-=1
            if left == -1 and x3 <= x1 <= x4:
                left = y-y2
            if right == -1 and x3 <= x2 <= x4:
                right = y-y2
            if left != -1 and right != -1:
                break
        pillar_lenght += (left if left != -1 else y)+(right if right != -1 else y)
    return pillar_lenght

platforms = (tuple(map(int,input().split())) for i in range(int(input())))

print(length(sorted(platforms)))

