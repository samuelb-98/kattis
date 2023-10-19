import sys

rows = r"1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./".upper()
for line in sys.stdin:
    output = ""
    line = line.strip()
    for x in line:
        if x != " ":
            output += rows[rows.index(x)-1]
        else:
            output += " "
    print(output)
    