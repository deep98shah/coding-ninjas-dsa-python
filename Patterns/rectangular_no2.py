"""
n = 5
1    2   3    4   5
 11   12  13   14  15
 21   22  23   24  25
 16   17  18   19  20
 6    7    8   9   10
"""
n = int(input())

start = 1
i = 1
while i <= n:
    for j in range(start, start+n):
        print(j, end=' ')
        j += 1
    if i == (n+1)//2:
        if n%2==0:
            start = n*(n-1) + 1
        else:
            start = n*(n-2) + 1
    elif i > (n+1)//2:
        start = start-n*2
    else:
        start = start+n*2
    i += 1
    print()
