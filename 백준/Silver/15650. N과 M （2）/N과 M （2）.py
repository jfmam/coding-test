import sys
input = sys.stdin.readline
n,m = map(int, input().split())

answer = []
ch = [0] * (n+1)
def dfs(L, st, selected):
    if L == m:
        a = " ".join(map(str, selected[:]))
        answer.append(a)
        return
    for i in range(st+1,n+1):
        if i not in selected:
            selected.append(i)
            dfs(L+1, i, selected)
            selected.pop()
dfs(0,0, [])

print(*answer, sep="\n")