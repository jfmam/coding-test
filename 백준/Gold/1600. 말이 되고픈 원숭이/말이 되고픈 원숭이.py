import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
m,n= map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
visited =  [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
q = deque([(0,0,k)])
move = [(0,1),(1,0),(0,-1),(-1,0)]
h_move = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
answer = float('inf')

while q:
    i,j,h = q.popleft()
    if i == n-1 and j == m-1:
        answer =  min(answer, visited[i][j][h])
        continue
    for k in move:
        ii = i + k[0]
        jj = j + k[1]
        if 0 <= ii < n and 0 <= jj < m and a[ii][jj] == 0:
            if visited[ii][jj][h] == 0:
                visited[ii][jj][h] = visited[i][j][h] + 1
                q.append((ii,jj,h))
    for k in h_move:
        if h == 0:
            break
        ii = i + k[0]
        jj = j + k[1]
        if 0 <= ii < n and 0 <= jj < m and a[ii][jj] == 0:
            if visited[ii][jj][h-1] == 0:
                visited[ii][jj][h-1] = visited[i][j][h] + 1
                q.append((ii,jj,h-1))

print(answer if answer != float('inf') else -1)             
                
