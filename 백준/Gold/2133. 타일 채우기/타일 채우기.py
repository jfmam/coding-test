import sys
input = sys.stdin.readline

n = int(input())
d = [0] * 31
d[2] = 3

for i in range(4, n+1):
    if i % 2 == 0:
        d[i] = d[i-2] * 3 + sum(d[:i-2]) * 2 + 2
print(d[n])