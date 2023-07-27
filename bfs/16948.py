# 데스 나이트

import sys
from collections import deque

n = int(input())
i1,j1,i2,j2 = map(int,input().split())
q = deque([(i1,j1,0)])
move = [(-2, -1), (-2, +1), (0, -2), (0, 2), (2, -1), (2, 1)]
visited = [[0] * n for _ in range(n)]
visited[i1][j1] = 1
while q:
    i,j,cnt = q.popleft()
    
    if i == i2 and j == j2:
        print(cnt)
        exit(0)
    else:
        for k in move:
            ii = k[0] + i
            jj = k[1] + j
            if 0 <= ii < n and 0 <= jj < n:
                if visited[ii][jj] == 0:
                    visited[ii][jj] = 1
                    q.append((ii,jj, cnt + 1))

                
print(-1)