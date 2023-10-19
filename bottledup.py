v,a,b = list(map(int,input().split()))

for y in range(v//b+1):
    x = (v-b*y)

    if x/a == int(x/a):
        print(int(x/a),y)
        quit()
print("Impossible")