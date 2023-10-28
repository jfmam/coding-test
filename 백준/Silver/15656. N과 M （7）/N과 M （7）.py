import sys
input = sys.stdin.readline

n,m = map(int, input().split())
a = list(map(int, input().split()))
answer = []
a.sort()
def dfs(level, selected):
    if level == m:
        answer.append(" ".join(map(str,selected)))
        return
    else:
        for i in range(n):
            selected.append(a[i])
            dfs(level+1, selected)
            selected.pop()
dfs(0,[])
print(*answer, sep="\n")