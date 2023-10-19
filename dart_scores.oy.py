score = int(input())

def search(score):
    bruh = ["single", "double", "triple"]
    for x in range(1,4):
        for i in range(1,21):
            for y in range(1,4):
                for j in range(1,21):
                    for z in range(1,4):
                        for k in range(1,21):
                            if score == x*i + y*j + z*k:
                                print(bruh[x-1],i)
                                print(bruh[y-1],j)
                                print(bruh[z-1],k)
                                return(True)
    return(False)

if score == 1:
    print("single", 1)

elif score == 2:
    print("single", 2)

else:
    if not search(score):
        print("impossible")
    