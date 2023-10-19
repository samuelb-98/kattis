import sys

low = 1
high = 1000
guess = (low + high) //2
print(guess, flush=True)

for line in sys.stdin:
    line=line.strip()
    if line == "lower":
        high = guess-1
    elif line == "higher":
        low = guess+1
    else:
        break
    guess = (low + high) //2
    print(guess, flush=True)