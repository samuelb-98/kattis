line = input().strip() + " "
for i in range(len(line)-1):
    if line[i] in [':',';']:
        if line[i+1] == ')':
            print(i)
        if line[i+1] == '-' and line[i+2] == ')':
            print(i)