import sys
from collections import deque
input = sys.stdin.readline

f,s,g,u,d = map(int, input().split()) # 총 층, 현재 층, 스타트링크 층, 위로 이동, 아래로 이동
ch = [-1] * (f+1)
q = deque([s])
ch[s] = 0
while q:
    v = q.popleft()
    if v == g:
        print(ch[v])
        exit(0)
    u_move = v + u
    d_move = v - d
    if 0 < u_move <= f and ch[u_move] == -1:
        ch[u_move] = ch[v] + 1
        q.append(u_move)
    if 0 < d_move <= f and ch[d_move] == -1:
        ch[d_move] = ch[v] + 1
        q.append(d_move)
print("use the stairs")
    