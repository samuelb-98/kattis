p = input().strip()
s = input().strip()

if p == s:
    print("Yes")
    quit()

for i in range(10):
    if str(i)+s == p:
        print("Yes")
        quit()
    if s+str(i) == p:
        print("Yes")
        quit()
new = ""
for c in s:
    if c == c.lower():
        new += c.upper()
    else:
        new += c.lower()

if new == p:
    print("Yes")
    quit()

print("No")