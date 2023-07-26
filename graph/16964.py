import sys
from collections import deque
sys.setrecursionlimit(100000)


def dfs(graph, visited, cmp):
    tmp = cmp.popleft()
    if not cmp: # cmp가 모두 비면 dfs 작동가능
        print(1)
        exit(0)
    # else
    visited[tmp] = True # 방문처리
    # cmp는 next_node
    for _ in range(len(graph[tmp])): # 현재노드에서 갈 수 있는 부분 접근, 1 3 2 4의 경우 children의 수만큼 이동이 가능해야한다.
        # 예시코드로 보았을 때 처음 3 -> 2 순서로 들어가야하기 떄문에 반복문이 꼭 필요하다.
        if cmp[0] in graph[tmp] and not visited[cmp[0]]: # 벙문을 하지 않았고 다음노드가 queue안에 있는지 체크
            dfs(graph, visited, cmp)
    return False


N = int(sys.stdin.readline())
visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]

for i in range(1, N):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

cmp = deque(map(int, sys.stdin.readline().split()))
if cmp[0] != 1:
    print(0)
    exit(0)
if not dfs(graph, visited, cmp):
    print(0)