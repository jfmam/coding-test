import sys
input = sys.stdin.readline
n,m = map(int, input().split())
answer = []

def dfs(level, selected):
    if level == m:
        answer.append(" ".join(map(str,selected[:])))
        return
    else:
        for i in range(1, n+1):
            selected.append(i)
            dfs(level+1, selected)
            selected.pop()
dfs(0, [])
print(*answer, sep="\n")
