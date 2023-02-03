import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
a = [[0] * (n+1) for _ in range(n+1)]
ch = [0] * (n+1)
# print(a)
for _ in range(m):
    b, c = map(int, input().split())
    a[b][c] = 1
    a[c][b] = 1
q = deque([1])
ch[1] = 1

while q:
    v = q.popleft()
    for i in range(n+1):
        if a[v][i] == 1 and ch[i] == 0: # ch를 통해 한번 방문하였던 곳을 또 방문하지 않게 해준다.
            # a[v][i] = a[i][v] = 0 # a[v][i]에 방문했을 때 a[i][v]에 또 방문하지 않게 하기 위해서
            q.append(i)
            ch[i] = 1 # 한 번 방문했던 곳을 표시해준다
cnt = 0
for i in range(2, n+1):
    if ch[i] != 0:
        cnt += 1
print(cnt)
