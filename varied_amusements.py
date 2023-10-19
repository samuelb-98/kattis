

line = [int(i) for i in input().split()]

N, a, b, c = line
total = 0
def pog(depth,a,b,c,prev,current):
    global N, total
    print(depth)
    if depth < N:
        for ride in ["a","b","c"]:
            if ride == prev:
                continue
            if ride == "a" and 0 < a:
                pog(depth+1,a-1,b,c,"a",current*a)
            if ride == "b" and 0 < b:
                pog(depth+1,a,b-1,c,"b",current*b)
            if ride == "c" and 0 < c:
                pog(depth+1,a,b,c-1,"c",current*c)
            print("fail at", depth)
    else:
        total += current
        print(current, "bruh")

pog(0,a,b,c,"bruh",1)
print(total)