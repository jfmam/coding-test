import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
a = []
pos = []
for i in range(n):
    tmp = input().rstrip()
    tmp2 = []
    for j,v in enumerate(tmp):
        tmp2.append(int(v))
        if v == '1':
            pos.append((i,j))
    a.append(tmp2)

move = [(0,1), (1,0), (0,-1), (-1,0)]
def bfs():
    q = deque([(0,0,0)])
    visited[0][0][0] = 1
    while q:
        i,j,break_wall = q.popleft()
        if i == n-1 and j == m-1:
            return visited[i][j][break_wall]
        else:
            for k in move:
                ii = i + k[0]
                jj = j + k[1]
                if 0 <= ii < n and 0 <= jj < m:
                    if visited[ii][jj][break_wall] == 0 and a[ii][jj] == 0:
                        visited[ii][jj][break_wall] = visited[i][j][break_wall] + 1
                        q.append((ii,jj, break_wall))
                    elif break_wall == 0 and a[ii][jj] == 1: 
                        visited[ii][jj][1] = visited[i][j][0] + 1
                        q.append((ii,jj,1))
    return -1                    
    
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

print(bfs())
            