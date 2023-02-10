import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, (input().split())))
a.sort()

s = 0
for i in range(n, 0, -1):
    s += (i * a[n-i])
print(s)
