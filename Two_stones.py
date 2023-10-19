import sys

for number in sys.stdin:
    if int(number) % 2 == 0:
        print("Bob")

    else:
        print("Alice")
        