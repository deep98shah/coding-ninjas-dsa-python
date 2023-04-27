"""
n = 4
4444444
4333334
4322234
4321234
4322234
4333334  
4444444
"""

n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(n-j+1, end='')
        j += 1
    k = 1
    while k <= n-i:
        print(n-i+1, end='')
        k += 1
    l = 1
    while l <= n-i:
        print(n-i+1, end='')
        l += 1
    m = 1
    no = n-i+2
    while m <= i-1:
        print(no, end='')
        no += 1
        m += 1
    i += 1
    print()
i = 1
while i <= n-1:
    j = 1
    no = n
    while j <= n-i:
        print(no, end='')
        no -= 1
        j += 1
    k = 1
    while k <= i:
        print(i+1, end='')
        k += 1
    l = 1
    while l <= i:
        print(i+1, end='')
        l += 1
    m = 1
    no = n-i
    while m <= n-i-1:
        print(no, end='')
        no += 1
        m += 1
    i += 1
    print()

    