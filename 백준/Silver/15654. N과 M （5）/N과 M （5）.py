import sys
input = sys.stdin.readline
n,m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
answer = []
ch = [0] * 9

def dfs(level, selected):
    if level == m:
        answer.append(" ".join(map(str, selected[:])))
        return
    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                selected.append(a[i])
                dfs(level+1, selected)
                selected.pop()
                ch[i] = 0
dfs(0,[])
print(*answer, sep="\n")