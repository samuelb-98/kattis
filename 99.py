import sys

print(1,flush=True)
for line in sys.stdin:
    line = int(line.strip())
    if line > 98:
        break
    if line % 3 == 1:
        print(line + 2,flush=True)
        if line + 2 > 98:
            break
    elif line % 3 == 2:
        print(line + 1,flush=True)
        if line + 1 > 98:
            break
    else:
        print(line + line%2 + 1,flush=True)

exit()