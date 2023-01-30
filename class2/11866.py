import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
a = deque([i for i in range(1, n+1)])
res = []
cnt = 1

while len(a) != 0:
    if cnt == m:
        res.append(a.popleft())
        cnt = 1
    else:
        a.append(a.popleft())
        cnt += 1

print("<", end='')
print(*res, sep=', ',end='')
print(">", end='')
