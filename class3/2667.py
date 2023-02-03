import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
    a = input().rstrip()
    b = []
    for j in a:
        b.append(int(j))
    board.append(b)

move = [(1, 0), (0, -1), (-1, 0), (0, 1)]

res = []
def find(x, y):
    board[x][y] = 0
    q = deque([(x, y)])
    cnt = 1
    while q:
        v = q.popleft()
        for i in move:
            xx = i[0] + v[0]
            yy = i[1] + v[1]
            if 0 <= xx < n and 0 <= yy < n:
                if board[xx][yy] == 1:
                    q.append((xx,yy))
                    cnt += 1
                    board[xx][yy] = 0

    res.append(cnt)

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            find(i,j)
res.sort()
print(len(res),*res, sep="\n")