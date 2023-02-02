import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [[0 for _ in range(n+1)] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    board[b][a] = board[a][b] = 1

def bfs(num):
    q = deque([num])
    ch[num] = 1
    while len(q) != 0:
        s = q.popleft()
        for i in range(1, n+1):
            if ch[i] != 0 and board[s][i] == 1 and s != i:
                ch[i] = ch[s] + 1 # 이전레벨에서 1을 더해준다.
                q.append(i)

res = []
for i in range(1, n+1):
    ch = [0] * (n+1)
    bfs(i)
    res.append(sum(ch))
print(res.index(min(res))+1)
