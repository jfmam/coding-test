import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
board = []
q = deque([])

cnt = 0
x, y, size = 0, 0, 2
for i in range(n):
    a = list(map(int, input().split()))
    board.append(a)
    for j in range(n):
        if board[i][j] == 9:
            x = i
            y = j


move = [(1, 0), (0, -1), (-1, 0), (0, 1)]
def biteFish(x, y, shark_size):
    dis = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    temp = []

    while q:
        a, b = q.popleft()
        for i in move:
            xx = a + i[0]
            yy = b + i[1]
            if 0 <= xx < n and 0 <= yy < n and visited[xx][yy] == 0:
                if board[xx][yy] <= shark_size:
                    q.append((xx, yy))
                    visited[xx][yy] = 1
                    dis[xx][yy] = dis[a][b] + 1
                    if board[xx][yy] < shark_size and board[xx][yy] != 0:
                        temp.append((xx, yy, dis[xx][yy]))
                        
    return sorted(temp, key=lambda x: (-x[2], -x[0], -x[1]))
res = 0
while 1:
    shark = biteFish(x,y,size)
    
    # 더 이상 먹을게 없을 때 break
    if len(shark) == 0:
        break
    
    
    xx,yy,dis = shark.pop()
    # 움직인 칸 수 더해주기
    res += dis
    board[xx][yy],board[x][y] = 0,0
    
    # 상어 좌표 옮기기
    x,y = xx,yy
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0
print(res)