from collections import deque
import sys
read = sys.stdin.readline


def bfs(v):
    q = deque()
    q.append(v)
    visit_list[v] = 1
    while q:
        v = q.popleft() # 0번째 출력
        print(v, end=" ")
        for i in range(1, n + 1): # 브루트포스 노드 최대 수만큼 범위 돌기
            if visit_list[i] == 0 and graph[v][i] == 1:
                q.append(i) # 0번쨰와 연결된 같은 레벨의 노드들 모두 q에 저장
                visit_list[i] = 1 # 방문여부 표시


def dfs(start):
    visit_list2[start] = 1
    print(v, end=" ")
    for end in range(1, n + 1): # 브루트포스 노드 최대수 만큼 범위 돌기
        if visit_list2[end] == 0 and graph[start][end] == 1:
            dfs(end)


n, m, v = map(int, read().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
visit_list = [0] * (n + 1)
visit_list2 = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, read().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)
