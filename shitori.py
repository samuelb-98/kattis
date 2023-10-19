n = int(input().strip())
used = set()
first = input().strip()
prev = first[-1]
used.add(first)
words = []
for i in range(n-1):
    w = input().strip()
    words.append(w)

counter = 0
for w in words:
    if w[0] != prev or w in used:
        if not counter%2:
            print("Player 2 lost")
            quit()
        else:
            print("Player 1 lost")
            quit()
    used.add(w)
    prev = w[-1]
    counter +=1
print("Fair game")