"""
n=4
1
11
121
1221

n=5
1
11
121
1221
12221
"""


n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        if i == 1:
            print(i, end='')
        elif j == 1 or j == i:
            print('1', end='')
        else:
            print('2', end='')
        j += 1
    print()
    i += 1