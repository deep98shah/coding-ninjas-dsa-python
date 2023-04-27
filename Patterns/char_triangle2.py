"""
E
DE
CDE
BCDE
ABCDE
"""

n = int(input())
i = 1
while i <= n:
    j = 1
    c = ord('A') + n-i
    while j <= i:
        print(chr(c), end='')
        j += 1
        c += 1
    print()
    i += 1