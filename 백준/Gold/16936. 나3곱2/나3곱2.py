import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
tmp = sorted(a)
Min = min(a)
Max = max(a)

def dfs(idx, visited, x):
    if idx == n:
        s_visited = sorted(visited)
        if s_visited == tmp:
            print(*visited, sep=" ")
            exit(0)
    else:
        if x * 2 not in visited and x * 2 in a:
            visited.append(x * 2)
            dfs(idx + 1, visited, x * 2)
            visited.pop()
        if x % 3 == 0:
            if x // 3 not in visited and x // 3 in a:
                visited.append(x // 3)
                dfs(idx + 1, visited, x // 3)
                visited.pop()

for i in a:
    dfs(1, [i], i)
