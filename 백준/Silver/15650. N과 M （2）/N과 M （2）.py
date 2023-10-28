import sys
input = sys.stdin.readline
n,m = map(int, input().split())

ch = [0] * 9
answer = []
def dfs(level, st, selected):
    if level == m:
        answer.append(" ".join(map(str, selected[:])))
        return
    else:
        for i in range(st, n+1):
            if ch[i] == 0:
                ch[i] = 1
                selected.append(i)
                dfs(level+1, i+1, selected)
                selected.pop()
                ch[i] = 0
dfs(0,1,[])
print(*answer, sep="\n")