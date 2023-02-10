import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
ch = [i for i in range(n+1)]
visited = [True] * (n+1)
board = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    board[a][b] = 1
    board[b][a] = 1

for i in range(1, n+1):
    q = deque([])
    q.append(i)
    while q:
        v = q.popleft()
        for j in range(1, n+1):
            if board[v][j] == 1 and visited[j]:
                q.append(j)
                ch[j] = ch[v]
                visited[j] = False
                board[v][j] = board[j][v] = 0
cnt = len(set(ch)) - 1
print(cnt)
