import sys
input = sys.stdin.readline
n,m = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))
a.sort()
s,e = 0,0
Min = float('inf')
while s < n and e < n:
    if a[e] - a[s] < m:
        e += 1
    else:
        Min = min(Min, a[e]-a[s])
        s += 1
print(Min)