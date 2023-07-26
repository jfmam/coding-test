
from collections import deque
import sys
input = sys.stdin.readline

start = 1 # 시작점
N = int(input())
graph = [[] for _ in range(N+1)]
visited = [-1 for _ in range(N+1)] # BFS시 탐색 여부 확인을 위함
children = [set() for _ in range(N+1)] # 트리의 부모자식 관계를 알기 위함
for _ in range(N-1): # 그래프 생성
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
test_case = list(map(int,input().split())) # 비교할 탐색 루트

# BFS
queue = deque()
queue.append(start)
visited[start] = 0
while queue:
    x = queue.popleft()
    for i in graph[x]:
        if visited[i] == -1:
            visited[i] = visited[x] + 1
            children[x].add(i) # 자식노드를 set 배열에 저장한다.
            queue.append(i)


next_index = 1
for i in test_case:
    if next_index == N:
        break
    c_length = len(children[i]) #자식의 길이
    c1 = set(test_case[next_index : next_index+c_length]) # test case에서 같은레벨만큼 추출한다.
    c2 = children[i] # 자식 노드
    if c1 != c2: # set끼리 비교함으로 순서가 달라도 문제가 되지 않는다.
        print(0)
        exit()
    next_index += c_length
print(1)