import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
virus = []
for i in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)
    for j, v in enumerate(tmp):
        if v == 2:
            virus.append((i, j))

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
Max = float("-inf")

def setVirus(board):
    q = deque([])
    for i, j in virus:
        q.append((i, j))
    while q:
        v = q.popleft()
        for k in move:
            ii = v[0] + k[0]
            jj = v[1] + k[1]
            if 0 <= ii < n and 0 <= jj < m:
                if board[ii][jj] == 0:
                    board[ii][jj] = 2
                    q.append((ii, jj))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                cnt += 1
    return cnt

def setWall(idx):
    global Max
    if idx == 3:
        board = deepcopy(a)
        Max = max(Max, setVirus(board))
        return
    else:
        for i in range(n):
            for j in range(m):
                if a[i][j] == 0:
                    a[i][j] = 1
                    setWall(idx + 1)
                    a[i][j] = 0

setWall(0)
print(Max)
