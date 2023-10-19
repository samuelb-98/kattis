n = int(input().strip())

if n < 100:
    print(99)
else:

    if n%100 < 49:
        print(n-n%100-1)
    else:
        print(n-n%100+99)