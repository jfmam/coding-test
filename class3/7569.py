import sys
from collections import deque
input = sys.stdin.readline
n, m, h = map(int, input().split())
board = []
for _ in range(h):
    b = []
    for _ in range(m):
        a = list(map(int, input().split()))
        b.append(a)
    board.append(b)

q = deque([])
for k in range(h): # 높이가 처음와야 된다!! (이거 꼬이면 답없음)
    for i in range(m): 
        for j in range(n):
            if board[k][i][j] == 1:
                q.append((k, i, j))

move = [(0, 1, 0), (0, 0, -1), (0, -1, 0), (0, 0, 1), (1, 0, 0), (-1, 0, 0)]
while q:
    v = q.popleft()
    for i in move:
        z = i[0] + v[0]
        x = i[1] + v[1]
        y = i[2] + v[2]
        if 0 <= x < m and 0 <= y < n and 0 <= z < h:
            if board[z][x][y] == 0:
                board[z][x][y] = board[v[0]][v[1]][v[2]] + 1
                q.append((z, x, y))
flag = True
for k in range(h):
    for i in range(m):
        for j in range(n):
            if board[k][i][j] == 0:
                flag = False
if flag:
    Max = -99999999
    for k in range(h):
        for i in range(m):
            mValue = max(board[k][i])
            Max = max(mValue, Max)
    print(Max - 1)
else:
    print(-1)
