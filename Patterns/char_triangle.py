"""
A
BC
CDE
DEFG
"""
n = int(input())
i = 1
while i <= n:
    j = i
    c = ord('A') + i-1
    while j >= 1:
        print(chr(c), end='')
        j -= 1
        c += 1
    print()
    i += 1