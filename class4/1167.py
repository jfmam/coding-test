import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
board = []
ch = [[0] * n for _ in range(m)]
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(m):
    temp = []
    a = input().rstrip()
    for j in range(len(a)):
        temp.append(int(a[j]))
    board.append(temp)
q = deque([(0, 0, 0)])

while q:
    x, y, cnt = q.popleft()
    if x == m-1 and y == n-1:
        print(cnt)
        break
    for i in move:
        ii = x + i[0]
        jj = y + i[1]
        if 0 <= ii < m and 0 <= jj < n:
            if ch[ii][jj] == 0:
                ch[ii][jj] = 1
                if board[ii][jj] == 0:
                    q.appendleft((ii, jj, cnt))
                else:
                    q.append((ii, jj, cnt+1))
