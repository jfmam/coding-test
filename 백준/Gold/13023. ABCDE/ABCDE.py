import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n,m = map(int, input().split())
a = [[] for _ in range(n)]
for _ in range(m):
    b,c = map(int, input().split())
    a[b].append(c)
    a[c].append(b)
visited = [0] * n
result = 0

def dfs(cur, length):
    global result
    for i in a[cur]:
        if length == 5:
            result = 1
            return
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, length + 1)
            visited[i] = 0

for i in range(n):
    if visited[i] == 0:
        visited[i] = 1
        dfs(i,1)
        visited[i] = 0
    if result == 1:
        break
print(result)
        