import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
d = [[i for i in a] for _ in range(2)]

for i in range(1,n):
    d[0][i] = max(d[0][i-1] + a[i], d[0][i])
    d[1][i] = max(d[0][i-1], d[1][i-1] + a[i])
print(max(max(d[0]), max(d[1])))