n = int(input())
a = [0] * (1001)
a[1] = 1
a[2] = 3

if n <= 2:
    print(a[n])
else:
    for i in range(3, n+1):
        a[i] = (a[i-1] + (2*a[i-2])) % 10007
    print(a[n])
