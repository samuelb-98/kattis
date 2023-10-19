
def solve(s):
    i = 0
    left = len(s)
    while left:
        n = 0    
        while s[i-n] == s[i+1+n]:
            left -=2
            n+=1
        i+=1
        if i <= left:
            i = 0

n = int(input().strip())
s = list(map(int,input().split()))
i = 0
while len(s):
    