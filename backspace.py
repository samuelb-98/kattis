i = [x for x in input().strip()]
counter = 0
for x in range(1,len(i)+1):
    if i[-x] == "<":
        i[-x] = " "
        counter += 1
    elif counter > 0:
        i[-x] = " "
        counter -=1

string = "".join(i)
string = string.replace(" ","")
print(string)