"""
1
21
321
4321
"""

n = int(input())
i = 1
while i <= n:
    j = i
    while j >= 1:
        print(j, end='')
        j -= 1
    print()
    i += 1