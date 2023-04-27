"""
n=5 (odd)
..*
.***
*****
.***
..*
"""

n = int(input())
n1 = (n//2) + 1
n2 = n//2
i = 1
while i <= n1:
    s = 1
    while s <= n1-i:
        print(' ', end='')
        s += 1
    j = 1
    while j <= i:
        print('*', end='')
        j += 1
    s = 1
    while s <= i-1:
        print('*', end='')
        s += 1
    print()
    i += 1
i = 1
while i <= n2:
    s = 1
    while s <= i:
        print(' ', end='')
        s += 1
    j = 1
    while j <= n2-i+1:
        print('*', end='')
        j += 1
    s = 1
    while s <= n2-i:
        print('*', end='')
        s += 1
    print()
    i += 1
