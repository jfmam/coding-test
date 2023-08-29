import sys
from math import sqrt
from collections import deque

input = sys.stdin.readline
t = int(input())
ch = [0] * 10001
for i in range(2, int(sqrt(10000)) + 1):
    j = 2
    while i * j <= 10000:
        ch[i * j] = 1
        j += 1
ch[0],ch[1] = 1,1
    
def bfs(start,end):
    q = deque([(start,0)])
    visited = [0] * 10001
    visited[start] = 1
    
    while q:
        v, cnt = q.popleft()
        strV = str(v)
        
        if v == end:
            return cnt
        for i in range(4): # 자릿수
            for j in range(10): # 0 ~ 9
                # 각 자릿수에 0 ~ 10까지 수를 넣어본다.
                temp = int(strV[:i] + str(j) + strV[i+1:])
                
                if visited[temp] == 0 and ch[temp] == 0 and temp >= 1000:
                    visited[temp] = 1
                    q.append((temp, cnt + 1))
    return -1
for _ in range(t):
    a,b = map(int, input().split())
    
    result = bfs(a,b)
    print(result if result != -1 else "Impossible")
    