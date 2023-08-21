# 한 노드로 부터 둘로 분할 했을 때 두 노드끼리는 이어져 있으면 안된다.
# 결론적으로 색을 칠했을 때 2가지 색으로 모두 칠할 수 있으면 된다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
t = int(input())

def dfs(cur):
    global result
    
    for i in a[cur]:
        if visited[i] == -1:
            visited[i] = 1 - visited[cur]
            dfs(i)

        elif visited[i] == visited[cur]:
            result = False
            return
answer = []
for _ in range(t):
    v,e = map(int, input().split()) # v:노드 개수 e: 간선개수
    a = [[] for _ in range(v+1)]
    visited = [-1] * (v+1) # visited...
    for _ in range(e):
        b,c = map(int, input().split())
        a[b].append(c)
        a[c].append(b)
    result = True
    
    for i in range(1, v+1):
        if visited[i] == -1:
            visited[i] = 1
            dfs(i)
            if not result:
                break
    
    if result:
        answer.append("YES")
    else:
        answer.append("NO")
print(*answer, sep="\n")
    
    