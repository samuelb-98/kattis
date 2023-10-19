a,c,b = tuple(map(int,input().split()))
pog = dict()
done = set()
for i in range(a):
    pog[input().strip()] = 0
for i in range(b):
    name,score = input().split()
    pog[name] += int(score)
    if pog[name] >= c and name not in done:
        print(f"{name} wins!")
        done.add(name)
if not len(done):
    print("No winner!")