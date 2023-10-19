import sys

class Ferry():
    def __init__(self,l):
        self.side = -1
        self.length = l*100
        self.counter = 0

    def pick_up(self,cars):
        sum_len = 0
        while sum_len + first(cars) <= self.length and len(cars) > 0:
            sum_len += cars.pop(0)
        self.side *= -1
        self.counter +=1
        return cars

def first(cars):
    if len(cars) > 0:
        return cars[0]
    else: return 0


innr = 0
casenr = 0
cases = -1
m = -10
for line in sys.stdin:
    line = line.split()

    if innr == 0:
        cases = int(line[0])
    if innr == 1:
        l,m = [int(i) for i in line]
        ferry = Ferry(l)
        left = []
        right = []
    if 1 < innr <= m + 1:
        if line[1] == "left":
            left.append(int(line[0]))
        else:
            right.append(int(line[0]))
    
    if innr == m + 1:
        while len(left) > 0 or len(right) > 0:
            if ferry.side == -1:
                left = ferry.pick_up(left)
            else:
                right = ferry.pick_up(right)
        print(ferry.counter)

        innr = 0
        casenr +=1
    if casenr == cases:
        break
    innr+=1