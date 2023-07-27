# 돌그룹

import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline
a,b,c = map(int, input().split())
if (a+b+c) % 3 != 0:
    print(0)
    exit(0)
q = deque([(a,b,c)])
while q:
    v = list(q.popleft())

    if v[0] == v[1] and v[1] == v[2] and v[0]== v[2]:
        print(1)
        exit(0)
    if v[0] <= 0 or v[1] <= 0 or v[2] <= 0:
        continue
    for i in list(combinations([0,1,2], 2)):
        tmp1 = v[i[0]]
        tmp2 = v[i[1]]
        
        if tmp1 > tmp2:
            v[i[0]] -= v[i[1]]
            v[i[1]] *= 2
            q.append((v[0], v[1], v[2]))
        elif tmp1 < tmp2:
            v[i[1]] -= v[i[0]]
            v[i[0]] *= 2
            q.append((v[0], v[1], v[2]))
print(0)             