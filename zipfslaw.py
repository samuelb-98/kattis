import sys
import re


first = 0
for line in sys.stdin:
    if first == 0:
        n = int(line.strip())
        words = dict()
    elif line.strip() == "EndOfText":
        output = []
        for word in words:
            if words[word] == n:
                output.append(word)
        if len(output) == 0:
            print("There is no such word.")
        else:
            for x in sorted(output):
                print(x)
        print("\n")
        first = -1
    else:
        bruh = re.split("[^a-z]+", line.strip().lower())
        for word in bruh:
            if len(word) < 2:
                continue 
            if word in words:
                words[word] +=1
            else:
                words[word] = 1
    first +=1