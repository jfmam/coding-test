import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
a = {}
b = {}
for _ in range(n):
    c, d = map(int, input().split())
    a[c] = d
for _ in range(m):
    c, d = map(int, input().split())
    b[c] = d

ch = [0] * 101
q = deque([(1, 0)])

Min = 17
while q:
    v, cnt = q.popleft()
    if v == 100:
        Min = min(Min, cnt)
        break
    for i in range(6,0,-1):
        x = v+i
        if x <= 100 and ch[x] == 0: # ch 배열 사용, 먼저 ch에 도달 한 사람이 가장 최소의 값을 갖기 떄문에
            if x in a.keys():
                x = a[x] # check 사다리 부분은 cnt가 그대로이기 떄문에 x 값에 대입
            if x in b.keys():
                x = b[x] # check snake도 동일
            if ch[x] == 0:
                ch[x] = 1
                q.append((x, cnt+1))
print(Min)
