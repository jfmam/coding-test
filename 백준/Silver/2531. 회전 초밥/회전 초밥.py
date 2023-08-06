import sys
from collections import deque
input = sys.stdin.readline
n,d,k,c = map(int, input().split())
a = []
for _ in range(n):
    tmp =  int(input())
    a.append(tmp)
s,e,e_idx = 0,0,0
answer = float('-inf')
m = deque([])
while s < n:
    if e - s < k:
        m.append(a[e_idx])
        e_idx = (e_idx + 1) % n
        e += 1
    elif e - s > k :
        m.popleft()
        s += 1
    else:
        length = len(set(m))
        if c not in m:
            length += 1
        answer = max(answer, length)            
        m.append(a[e_idx])
        e_idx = (e_idx + 1) % n
        e += 1

print(answer)