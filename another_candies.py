import sys

def rolling_average(avg,new_value,n):
    avg -= avg/n
    avg += new_value/n
    return(avg)

first = True
second = False
test_cases = 0
average = 0
current_case = 0

for line in sys.stdin:
    line = line.strip()
    if current_case == 0:
        test_cases = int(line)
        current_case += 1
    else:    
        if line == "":
            n = 1
            if current_case != 1:
                if abs(average - int(average)) < 0.0000001 or abs(average - int(average)-1) < 0.0000001:
                    print("YES")
                else:
                    print("NO")
            current_case += 1
        else:
            average = rolling_average(average, int(line), n)
            n += 1