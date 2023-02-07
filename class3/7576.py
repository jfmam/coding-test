import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())
board = []
for _ in range(m):
    board.append(list(map(int, input().split())))

q = deque([])
for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            q.append((i, j))

move = [(1, 0), (0, -1), (-1, 0), (0, 1)]
while q:
    v = q.popleft()
    for i in move:
        x = v[0] + i[0]
        y = v[1] + i[1]
        if 0 <= x < m and 0 <= y < n:
            if board[x][y] == 0:
                board[x][y] = board[v[0]][v[1]] + 1
                q.append((x, y))

flag = True
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            flag = False

if flag:
    Max = max(board[0])
    for i in range(1,m):
        mValue = max(board[i])
        Max = max(mValue, Max)
    print(Max - 1)
else:
    print(-1)