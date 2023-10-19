n = int(input().strip())
ans = input().strip()

adc = 0
brc = 0
goc = 0

ad = "ABC"*n
br = "BABC"*n
go = "CCAABB"*n

for i in range(len(ans)):
    if ans[i] == ad[i]:
        adc +=1
    if ans[i] == br[i]:
        brc +=1
    if ans[i] == go[i]:
        goc +=1

winner = (max(adc,brc,goc))
print(winner)
if winner == adc:
    print("Adrian")
if winner == brc:
    print("Bruno")
if winner == goc:    
    print("Goran")