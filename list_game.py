X = int(input())


def primes(x):
    if x == 1:
        return([1])
    factors = []
    i = 3
    while x%2 == 0:
        x/=2
        factors.append(2)
    while x != 1 and i <= x**0.5+1:
        while x%i == 0:
            x/=i
            factors.append(i)
        i+=2
    if x != 1:
        factors.append(1)
    return(factors)

print(len(primes(X)))
