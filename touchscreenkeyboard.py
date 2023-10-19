import sys

keyboard = [
    list("qwertyuiop"),
    list("asdfghjkl"),
    list("zxcvbnm")]

print(keyboard)

innr = 0
cases = -1
casenr = 0
n = -10
for line in sys.stdin:
    if innr == 0:
        cases = int(line.split()[0])
    if innr == 1:
        word,n = line.split()
        n = int(n)
        suggs = []
    if 1 < innr <= n+1:
        suggs.append(line.strip())
    if innr == n+1:
        
        casenr +=1
        pass
    innr +=1