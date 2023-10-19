t = int(input().strip())
for c in range(t):
    input()
    input()
    a = max(list(map(int,input().split())))
    b = max(list(map(int,input().split())))

    if a < b:
        print("MechaGodzilla")
    else:
        print("Godzilla")