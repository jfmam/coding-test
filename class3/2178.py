import sys
from collections import deque
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
n, m = map(int, input().split())
board = []
ch = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    a = input().rstrip()
    b = []
    for j in a:
        b.append(int(j))
    board.append(b)
q = deque([(0, 0)])
move = [(1, 0), (0, -1), (-1, 0), (0, 1)]
ch[0][0] = 1
while q:
    a = q.popleft()
    x, y = a[0], a[1]
    if x == n-1 and y == m-1:
        print(ch[x][y])
        break
    for i in move:
        xx = x + i[0]
        yy = y + i[1]
        if xx >= 0 and xx < n and yy >= 0 and yy < m:
            if board[xx][yy] == 1:
                q.append((xx, yy))
                board[xx][yy] = 0
                ch[xx][yy] = ch[x][y] + 1
                
# dfs 시간초과로 인해 파이썬에서는 지양 ㅠ
# Min = 9999999

# def dfs(x, y, cnt):
#     if x == n-1 and y == m-1:
#         global Min
#         Min = min(Min, cnt)
#     else:
#         for i in move:
#             xx = x + i[0]
#             yy = y + i[1]
#             if xx >= 0 and xx < n and yy >= 0 and yy < m:
#                 if board[xx][yy] == 1:
#                     board[x][y] = 0
#                     dfs(xx, yy, cnt+1)

#                     board[x][y] = 1 # dfs 재귀 이후 다시 돌아올 때 board[x][y] = 1로 되돌려 놔준다.


# dfs(0, 0, 1)  # 0,0도 카운팅 해야한다!
# print(Min)
