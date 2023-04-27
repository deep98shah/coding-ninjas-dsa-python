"""
 A
 BB
 CCC
"""

n = int(input())
i = 1
while i <= n:
    j = 1
    c = ord('A') + i-1
    while j <= i:
        print(chr(c), end='')
        j += 1
    print()
    i += 1