
n = int(input())

def isprime(num):
    for n in range(2,int(num**1/2)+1):
        if num%n==0:
            return False
    return True    




record = 0
b = 2
while b < n:
    if isprime(b):
        print(b)
        digits = []
        while n > 0:
            digits.append(int(n % b))
            n //= b
        print(''.join(map(str, digits[::-1])))
    if b == 2:
        b += 1
    else:
        b += 2

