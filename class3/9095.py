import sys
input = sys.stdin.readline
test = int(input())
a = [0] * 12
for _ in range(test):
    n = int(input())
    a[1] = 1
    a[2] = 2
    a[3] = 4
    a[4] = 7
    if n <= 4:
        print(a[n])
    else:
        for i in range(5,n+1):
            a[i] = a[i-1] + a[i-2] + a[i-3]
        print(a[n])