import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
answer = []
move = [(-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1), (1,2),(2,1)]
for _ in range(t):
    n = int(input())
    board = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    x,y = map(int, input().split())
    board[x][y] = 1
    visited[x][y] = 1
    target_x, target_y = map(int, input().split())
    q = deque([(x,y)])
    while q:
        i,j = q.popleft()
        if i == target_x and j == target_y:
            answer.append(visited[i][j] - 1)
            break
        for k in move:
            ii = k[0] + i
            jj = k[1] + j
            if 0 <= ii < n and 0 <= jj < n:
                if visited[ii][jj] == 0:
                    visited[ii][jj] = visited[i][j] + 1
                    q.append((ii,jj))
print(*answer, sep="\n")