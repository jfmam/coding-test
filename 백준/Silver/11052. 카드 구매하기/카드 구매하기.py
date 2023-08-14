import sys
input = sys.stdin.readline
n = int(input())
a = [0] + list(map(int, input().split()))
d = [0] * (n+1)
d[1] = a[1]

for i in range(2,n+1):
    d[i]= a[i]
    for j in range(1, i):
        d[i] = max(d[j] + a[i-j], d[i])
print(d[n])