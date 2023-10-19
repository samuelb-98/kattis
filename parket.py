a,b = tuple(map(int,input().split()))
p = -(a+4)/2
q = (a+b)
y = -p/2 + ((p/2)**2-q)**0.5
x = (a+4-2*y)/2
print(round(y),round(x))