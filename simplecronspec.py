import sys

secs = [False for i in range(24*60*60)]
total = 0
progs = []


class CronSpec():
    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def count_starts(self):
        return len(self.hours)*len(self.minutes)*len(self.seconds)
    
    def starts(self):
        starts = []
        for h in self.hours:
            for m in self.minutes:
                for s in self.seconds:
                    starts.append(3600*h + 60*m + s)
        return starts


def listify(line,h):
    new = []
    if line == "*":
        if h:
            new = [i for i in range(24)]
        else:
            new = [i for i in range(60)]
    else:
        time = line.split(",")
        for t in time:
            if "-" in str(t):
                temp = [int(i) for i in t.split("-")]
                for i in range(temp[0],temp[1]+1):
                    new.append(i)
            else:
                new.append(int(t))
    return(new)

innr = 0
commands = -1
for line in sys.stdin:
    line = line.split()
    if innr == 0:
        commands = int(line[0])
    if 0 < innr <= commands:
        hours = listify(line[0],True)
        minutes = listify(line[1],False)
        seconds = listify(line[2],False)

        progs.append(CronSpec(hours,minutes,seconds))

    if innr == commands:
        for p in progs:
            total += p.count_starts()
            for s in p.starts():
                secs[s] = True

        print(secs.count(True),total)
        break
    innr +=1