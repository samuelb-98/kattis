t = int(input().strip())
for c in range(t):
    pizzas = int(input().strip())
    pog1 = dict()
    pog2 = dict()
    for p in range(pizzas):
        pizza = input().strip()
        foreign = input().split()[1:]
        eng = input().split()[1:]
        
        for f in foreign:
            if f in pog1:
                pog1[f].append(pizza)
            else:
                pog1[f] = [pizza]
        
        for f in eng:
            if f in pog2:
                pog2[f].append(pizza)
            else:
                pog2[f] = [pizza]

    ans = []
    for x in pog1:
        for y in pog2:
            if pog1[x] == pog2[y]:
                ans.append((x,y))
    
    for i,j in sorted(ans):
        print(f"({i}, {j})")
