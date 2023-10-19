import sys
hex_char = [str(i) for i in range(10)]
for x in ["a","b","c","d","e","f"]:
    hex_char.append(x)
    hex_char.append(x.upper())
for line in sys.stdin:
    line=line.strip()
    line+=" "
    for char in range(len(line)-1):
        if line[char] == "0" and ( line[char+1] == "x" or line[char+1] == "X" ):
            i = 2
            current = "0x"
            while line[char+i] in hex_char:
                current += line[char+i]
                i +=1
            print(current, int(current,16)) 
            
