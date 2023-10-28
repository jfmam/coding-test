import sys
input = sys.stdin.readline
n,m = map(int, input().split())
answer= []

def dfs(level, st, selected):
    if level == m:
        answer.append(" ".join(map(str, selected[:])))
        return
    else:
        for i in range(st,n+1):
            selected.append(i)
            dfs(level + 1, i, selected)
            selected.pop()
dfs(0,1,[])
print(*answer, sep="\n")