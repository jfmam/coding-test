from collections import deque
input = __import__('sys').stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    cnt = 1
    while q:
        i, j = q.popleft()
        zeros[i][j] = group # 몇번 그룹인지 숫자 넣기
        for idx in range(4):
            ni, nj = i + dy[idx], j + dx[idx]
            if ni < 0 or ni >= n or nj < 0 or nj >= m or visited[ni][nj] or graph[ni][nj] == 1:
                continue
            visited[ni][nj] = True # 방문
            q.append((ni, nj)) # append
            cnt += 1 # 갯수 올리기
    return cnt

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
zeros = [[0] * m for _ in range(n)]
group = 1
info = {} # 그룹
info[0] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            w = bfs((i, j)) # 아직 방문하지않고 0인상태 만나면 그룹의 0값구하기
            info[group] = w # 그룹의 0의갯수만큼 추가
            group += 1 # 그룹 1 ~

for i in range(n):
    for j in range(m):
        addList = set()
        if graph[i][j]:
            for idx in range(4):
                ni, nj = i + dy[idx], j + dx[idx]
                if ni < 0 or ni >= n or nj < 0 or nj >= m:
                    continue
                addList.add(zeros[ni][nj]) # 인접한 곳의 그룹의 몇번인지 addList에 추가
            for add in addList: # addList돌면서 값더하기
                graph[i][j] += info[add]
                graph[i][j] %= 10

for g in graph:
    print("".join(map(str, g)))