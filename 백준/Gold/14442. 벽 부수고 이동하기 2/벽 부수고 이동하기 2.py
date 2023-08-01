import sys
from collections import deque
input = sys.stdin.readline

n,m,k = map(int, input().split())
board = []
for i in range(n):
    board.append(input().rstrip())
visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
move = [(0,1),(1,0),(0,-1),(-1,0)]
q = deque([(0,0,k)])
visited[0][0][k] = 1
while q:
    i,j,wall= q.popleft()
    
    if i == n-1 and j == m-1:
        print(visited[i][j][wall])
        exit(0)
    else:
        for a in move:
            ii = i + a[0]
            jj = j + a[1]
            if 0 <= ii <n and 0<= jj < m:
                if wall > 0 and board[ii][jj] == '1' and visited[ii][jj][wall-1] == 0:
                    visited[ii][jj][wall-1] = visited[i][j][wall] + 1 
                    q.append((ii,jj, wall -1))
                elif board[ii][jj] == '0' and visited[ii][jj][wall] == 0:
                    visited[ii][jj][wall] = visited[i][j][wall] + 1
                    q.append((ii,jj,wall))
                    
print(-1)
