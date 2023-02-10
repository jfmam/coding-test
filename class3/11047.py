import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))
a.sort(reverse=True)

cnt = 0
while a:
    if k == 0:
        break
    if a[0] > k:
        a.pop(0)
        continue
    else:
        v = k // a[0]
        k -= (a[0] * v)
        cnt += v
print(cnt)