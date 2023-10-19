import sys
counter = 1
innr = 0
for line in sys.stdin:
    if line.strip() == "0":
        break
    if innr == 0:
        n = int(line.strip())
        names = []
        odds = []
    if 0 < innr <= n:
        names.append(line.strip())
    if innr == n:
        print("SET",counter)
        for i in range(n):
            if not i%2:
                print(names[i])
            else:
                odds.insert(0,names[i])
        for i in odds:
            print(i)
        
        counter +=1
        innr = -1
    innr +=1