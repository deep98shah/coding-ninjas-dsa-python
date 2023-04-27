"""
1111
000
11
0
"""
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n-i+1:
        if i % 2 == 1:
            print('1', end='')
        else:
            print('0', end='')
        j += 1
    i += 1
    print()