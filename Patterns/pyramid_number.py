"""
...1
..212
.32123
4321234
"""
n = int(input())

i = 1
while i <= n:
    s = 1
    while s <= n-i:
        print(' ', end='')
        s += 1
    j = i
    while j >= 1:
        print(j, end='')
        j -= 1
    s = 2
    while s <= i:
        print(s, end='')
        s += 1
    print()
    i += 1