"""
n = 4
...1
..232
.34543
4567654
"""

n = int(input())
i = 1
while i <= n:
    s = 1
    while s <= n-i:
        print(' ', end='')
        s += 1
    j = 1
    no = i
    while j <= i:
        print(no, end='')
        no += 1
        j += 1
    s = 1
    no = 2 * (i-1)
    while s <= i-1:
        print(no, end='')
        no -= 1
        s += 1
    print()
    i += 1