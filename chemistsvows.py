import sys

elem = ['b', 'c', 'f', 'h', 'i', 'k', 'n', 'o', 'p', 's', 'u', 'v', 'w', 'y', 'ac', 'ag', 'al', 'am', 'ar', 'as', 'at', 'au', 'ba', 'be', 'br', 'ca', 'cd', 'ce', 'cl', 'cm', 'cr', 'db', 'ds', 'dy', 'er', 'es', 'eu', 'fe', 'fl', 'fm', 'fr', 'ga', 'gd', 'ge', 'he', 'hg', 'ir', 'kr', 'la', 'li', 'lr', 'lu', 'lv', 'md', 'mg', 'mn', 'mo', 'mt', 'na', 'nd', 'ne', 'pa', 'pd', 'pm', 'pr', 'pt', 'ra', 'rb', 're', 'rf', 'rg', 'rh', 'rn', 'ru', 'se', 'sg', 'sm', 'sr', 'ta', 'tb', 'tc', 'te', 'th', 'ti', 'tl', 'tm', 'xe', 'zn', 'zr']

def solve(word):
    n = len(word)
    pog = [False for i in range(n)]

    for i in range(n):
        for e in elem:
            l = len(e)
            if l <= i+1:
                if l-1:
                    if e[1] == word[i] and e[0] == word[i-1] and (pog[i-2] or i == 1):
                        pog[i] = True
                        continue
                else:
                    if e == word[i] and (pog[i-1] or i == 0):
                        pog[i] = True
                        continue
    if pog[n-1]:
        print("YES")
    else:
        print("NO")
                

cases = int(input().strip()) 
for line in sys.stdin:
    solve(line.strip())
    cases -=1
    if cases == 0:
        break
    