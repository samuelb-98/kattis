import sys
words = []
innr = 0
prob = 0
P = -1
for line in sys.stdin:
    if innr == 0:
        P,T = [int(i) for i in line.split()]
        counter = 0
    if 0 < innr <= T:
        words.append(line.strip())
    if innr == T:
        wrong = False
        for word in words:
            if word[1:] != word[1:].lower():
                wrong = True
        if not wrong:
            counter += 1
        innr = 0
        prob+=1
        words = []
    if prob == P:
        break
    innr +=1

print(counter)