"""
n=4
*000*000*
0*00*00*0
00*0*0*00
000***000

n=3
*00*00*
0*0*0*0
00***00
"""

n = int(input())
n1 = 2*n+1
i = 1
while i <= n:
    start = i
    end = n1 - i + 1
    j = 1
    while j <= n1:
        if j in [start, end, n1//2+1]:
            print('*', end='')
        else:
            print('0', end='')
        j += 1
    i += 1
    print()


