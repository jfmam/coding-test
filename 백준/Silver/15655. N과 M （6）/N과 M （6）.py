import sys
input = sys.stdin.readline

n,m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ch = [0] * 9
answer= []
def dfs(level, st, selected):
    if level == m:
        answer.append(" ".join(map(str, selected[:])))
        return
    else:
        for i in range(st, n):
            if ch[i] == 0:
                ch[i] = 1
                selected.append(a[i])
                dfs(level+1, i+1, selected)
                selected.pop()
                ch[i] = 0
dfs(0,0,[])
print(*answer, sep="\n")