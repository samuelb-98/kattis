teas = int(input().strip())
tea_prices = tuple(map(int,input().split()))
toppings = int(input().strip())
topping_prices = tuple(map(int,input().split()))
comb = []
for i in range(teas):
    comb.append(tuple(map(int,input().split()[1:])))
money = int(input().strip())



best = 10000000
for i,p1 in enumerate(tea_prices):
    for j,p2 in enumerate(topping_prices):
        if j+1 in comb[i]:
            tot = p1 + p2
            if tot < best:
                best = tot
print(max(0,money//best-1))