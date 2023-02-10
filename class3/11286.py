import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
board = []
visited = [[0] * n for _ in range(n)]
q = deque([])
for _ in range(n):
    a = list(map(int, input().split()))
    for i in range(len(a)):
        if a[i] == 1:
            q.append(i)
    board.append(a)

def bfs(x):
    q = deque()
    q.append(x)
    ch = [0 for _ in range(n)]
    
    while q:
        v = q.popleft()
        
        for i in range(n):
            if ch[i] == 0 and board[v][i] == 1:
                q.append(i)
                ch[i] = 1
                visited[x][i] = 1
for i in range(n):
    bfs(i)
for i in visited:
    print(*i)