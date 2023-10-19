ua,ub,ra,rb = list(map(int,input().split()))
tot = 0
if ra != 0:
    tot += ub
if rb != 0:
    tot += ua
if ra + rb == 0:
    tot += min(ub,ua)
tot += ra*rb
print(tot)
