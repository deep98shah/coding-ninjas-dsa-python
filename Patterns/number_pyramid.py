"""
n = 6
123456
 23456
  3456
   456
    56
     6
    56
   456
  3456
 23456
123456
"""
n = int(input())
i = 1
while i <= n:
    s = 1
    while s <= i-1:
        print(' ', end='')
        s += 1
    j = i
    while j <= n:
        print(j, end='')
        j += 1
    i += 1
    print()
i = 1
while i <= n-1:
    s = 1
    while s <= n-i-1:
        print(' ', end='')
        s += 1
    j = n-i
    while j <= n:
        print(j, end='')
        j += 1
    i += 1
    print()