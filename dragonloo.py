import sys
import bisect

heads = []
knights = []
input_nr = 0

for line in sys.stdin:
    if line.strip() == "0 0":
        break
    if input_nr == 0:
        mission = []
        heads = []
        knights = []
        n,m = [int(i) for i in line.split()]
    if 0 < input_nr <= n:
        head = int(line.strip())
        bisect.insort(heads,head)
    if n < input_nr <= n+m:
        knight = int(line.strip())
        bisect.insort(knights,knight)
    if input_nr == n+m:
        for head in heads:
            for knight in knights:
                if knight >= head:
                    mission.append(knight)
                    knights = knights[knights.index(knight)+1:]
                    break
        
        doomed = False
        while len(mission) < n:
            if len(knights) == 0:
                print("Loowater is doomed!")
                doomed = True
                break
            else:
                mission.append(knights.pop(0))        
        
        if not doomed:
            print(sum(mission))

        input_nr = -1
    input_nr +=1