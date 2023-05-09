import sys
input = sys.stdin.readline
n, m = map(int, input().split())
ch = [0] * (n+1)
answer = []

def dfs(cnt, selected):
    if cnt == m:
        global answer
        answer.append(selected[:])
        return
    for i in range(1, n+1):
        if ch[i] == 0:
            ch[i] = 1
            selected.append(i)
            dfs(cnt+1, selected)
            selected.pop()
            ch[i] = 0
dfs(0,[])
