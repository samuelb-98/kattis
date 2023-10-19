import sys

L = -2
case = 1



input_nr = 0
for line in sys.stdin:
    if input_nr == 0:
        cases = int(line.split()[0])
    if input_nr == 1:
        N, M, L = [int(i) for i in line.split()]
        agencies = dict()
        prices = []
    if 1 < input_nr <= L+1:
        a = line.split(":")
        price = a[1].split(",")
        agencies[a[0]] = (int(price[0]), int(price[1]))
    if input_nr == L+1:
        for a in agencies:
            work = N
            min_cost = 0
            A, B = agencies[a]
            while 2*M <= work:
                if A * work//2 < B:
                    min_cost +=  A * work//2
                else:
                    min_cost += B
                work = work//2
            min_cost += A*(work-M)
            prices.append((a, min_cost))
        print("Case", case)
        for i in sorted(prices,key=lambda x:(x[1],x[0])):
            print(i[0], i[1])

        case += 1

        input_nr = 0
    input_nr +=1
