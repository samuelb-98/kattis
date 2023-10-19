import sys


def prime_factors(n):
    factors = []
    primes = set()
    while n%2 == 0:
        n //= 2
        factors.append(2)
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def pog(numbers):
    ans = 1
    factors = []
    primes = set()
    for x in numbers:
        factors.append(prime_factors(x))
    for x in factors:
        for p in x:
            primes.add(p)
    for p in list(primes):
        ans*= p**max([bruh.count(p) for bruh in factors])
        if ans > 10**9:
            return("More than a billion.")
    return(ans)



input_nr = 0
case_nr = 0
machines = 2

for line in sys.stdin:
    line = [int(i) for i in line.split()]
    if input_nr == 0:
        machines = line[0]
    if input_nr == 1:
        w = line[0]
    if input_nr == 2:
        print(pog(line))
        input_nr = 0
        case_nr +=1
    if case_nr == machines:
        break
    input_nr +=1