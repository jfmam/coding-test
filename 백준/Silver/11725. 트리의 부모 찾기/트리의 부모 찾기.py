import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline
n = int(input())
board = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(n-1):
    b,c = map(int, input().split())
    board[b].append(c)
    board[c].append(b)

def iter(current):
    for i in board[current]:
        if visited[i] == 0:
            visited[i] = current
            iter(i)
visited[1] = 1
iter(1)
for i in range(2,n+1):
    print(visited[i])