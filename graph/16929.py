import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = []
pos = []
for i in range(n):
    tmp = input().rstrip()
    a.append(tmp)
    for j,v in enumerate(tmp):
        if v == 'X':
            pos.append((i,j))
if len(pos) == 0:
    print(0)
    exit(0)
move = [(0,1), (1,0), (0,-1), (-1,0),(-1,1),(1,)]
visited = [[0] * n for _ in range(n)]
# 인접한 면에 X가 있으면 계속해서 칠해나가자
s = set([])
def color(si,sj):
    c = set([])
    global visited
    for i in move:
        ii,jj = si + i[0], sj+i[1]
        if 0 <= ii < n and 0 <= jj < n:
            c.add(visited[ii][jj])
    cList = list(c)
    Max = max(cList)
    for i in range(1, Max+2):
        if i not in cList:
            visited[si][sj] = i
            break


for i in pos:
    color(i[0], i[1])

for i in range(n):
    for j in range(n):
        s.add(visited[i][j]) 
print(len(s) - 1)