import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())
a = []
pos = []
for i in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)
    for j, v in enumerate(tmp):
        if v == 1:
            pos.append((i, j))

move = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

answer = -1

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            q = deque([(i, j)])
            visited = [[0] * m for _ in range(n)]
            while q:
                ii, jj = q.popleft()
                if a[ii][jj] == 1:
                    answer = max(answer, visited[ii][jj])
                    break
                for k in move:
                    ni = ii + k[0]
                    nj = jj + k[1]
                    if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0:
                        visited[ni][nj] = visited[ii][jj] + 1
                        q.append((ni, nj))

print(answer)
