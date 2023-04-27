"""
1........1
12......21
123....321
1234..4321
1234554321
"""

n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end='')
        j += 1
    s1 = 1
    while s1 <= n-i:
        print(' ', end='')
        s1 += 1
    s2 = 1
    while s2 <= n-i:
        print(' ', end='')
        s2 += 1
    k = i
    while k >= 1:
        print(k, end='')
        k -= 1
    print()
    i += 1