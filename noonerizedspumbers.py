line = input().split()
x,o,y,bruh,z = line

if o == "+":
    for i in range(1,len(x)):
        for j in range(1,len(y)):
            if int(y[:j] + x[i:]) + int(x[:i] + y[j:]) == int(z):
                print(int(y[:j] + x[i:]),o, int(x[:i] + y[j:]),bruh, int(z))
                quit()

    for i in range(1,len(x)):
        for j in range(1,len(z)):
            if int(z[:j] + x[i:]) + int(y) == int(x[:i] + z[j:]):
                print(int(z[:j] + x[i:]),o,int(y),bruh, int(x[:i] + z[j:]))
                quit()

    for i in range(1,len(y)):
        for j in range(1,len(z)):
            if int(z[:j] + y[i:]) + int(x) == int(y[:i] + z[j:]):
                print(int(x),o,int(z[:j] + y[i:]),bruh, int(y[:i] + z[j:]))
                quit()
else:
    for i in range(1,len(x)):
        for j in range(1,len(y)):
            if int(y[:j] + x[i:]) * int(x[:i] + y[j:]) == int(z):
                print(int(y[:j] + x[i:]),o, int(x[:i] + y[j:]),bruh, int(z))
                quit()

    for i in range(1,len(x)):
        for j in range(1,len(z)):
            if int(z[:j] + x[i:]) * int(y) == int(x[:i] + z[j:]):
                print(int(z[:j] + x[i:]),o, int(y),bruh, int(x[:i] + z[j:]))
                quit()

    for i in range(1,len(y)):
        for j in range(1,len(z)):
            if int(z[:j] + y[i:]) * int(x) == int(y[:i] + z[j:]):
                print(int(x),o,int(z[:j] + y[i:]),bruh, int(y[:i] + z[j:]))
                quit()