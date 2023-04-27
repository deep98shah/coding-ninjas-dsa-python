"""
 5432*
 543*1
 54*21
 5*321
 *4321
"""

n = int(input())
i = 1
p = n
while i <= n:
    j = 1
    while j <= n:
        if j == p:
            print('*', end='')
        else:
            print(n-j+1, end='')
        j += 1
    p -= 1
    i += 1
    print()