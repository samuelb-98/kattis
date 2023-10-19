import sys

for line in sys.stdin:
    output = ""
    prev = 0
    numbers = line.split()

    numbers.sort(key=lambda item: (len(item), item))

    while len(numbers[0]) < len(numbers[1]):
        numbers[0] = "0" + numbers[0]

    for i in range(1,len(numbers[0])+1):
        curr = (int(numbers[1][-i]) - int(numbers[0][-i]) - prev)%10
        if int(numbers[1][-i]) - int(numbers[0][-i]) - prev < 0:
            prev = 1
        else:
            prev = 0
        output = str(curr) + output
    while output[0] == "0"  and len(output) > 1:
        output = output[1:]
    print(output)