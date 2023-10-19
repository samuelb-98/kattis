n,m = [int(i) for i in (input().split())]

if n < m:
    if m-n == 1:
        print(f"Dr. Chaz will have {m-n} piece of chicken left over!")
    else:
        print(f"Dr. Chaz will have {m-n} pieces of chicken left over!")
else:
    if n-m == 1:
        print(f"Dr. Chaz needs {n-m} more piece of chicken!")
    else:
        print(f"Dr. Chaz needs {n-m} more pieces of chicken!")