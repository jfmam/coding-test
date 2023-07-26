import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input().rstrip())
a = [([] * (n+1)) for _ in range(n+1)]

for _ in range(n):
    b,c = map(int, input().split())
    a[b].append(c)
    a[c].append(b)

cycle = set([])
visited = [0] * (n+1)
flag = False
def findCycle(i,cnt,si):
    if cnt >= 3 and i == si:
        global flag
        for k,v in enumerate(visited):
            if v == 1:
                cycle.add(k)
        flag = True
        return
    else:
        for k in a[i]: # 꼭 다돌아야하나?
            if visited[k] == 0:
                visited[k] = 1
                findCycle(k, cnt+1, si)
                visited[k] = 0
                
for i in range(1, n+1): # 1~n+1중의 cycle 찾기
    findCycle(i, 0, i)
    if flag: # cycle이 하나니까 가능하다.
        break


def bfs(i,cnt):
    q = deque([(i,0)])
    global ans
    while q:
        v,cnt = q.popleft()
        if v in list(cycle):
            ans.append(cnt)
            return
        for j in a[v]:
            if bfsVisited[j] == 0:
                bfsVisited[j] = 1
                q.append((j, cnt+1))
                
                
ans = []
for i in range(1, n+1):
    bfsVisited = [0] * (n+1)
    if i in list(cycle):
        ans.append(0)
    else:
        bfs(i,0)
print(*ans)   
