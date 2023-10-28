import sys
input = sys.stdin.readline

n,m = map(int, input().split())
answer = []
visited = [0] * 9

def dfs(level, selected):
    if level == m:
        answer.append(selected[:])
        return
    else:
        for i in range(1, n+1):
            if visited[i] == 0:
                visited[i] = 1
                selected.append(i)
                dfs(level + 1, selected)
                selected.pop()
                visited[i] = 0
dfs(0,[])

for i in answer:
    print(*i, sep=" ")