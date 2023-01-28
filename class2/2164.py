from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
a = deque([i for i in range(1, n+1)])

while len(a) != 1:
    a.popleft()
    a.rotate(-1)
print(a[0])

# push와 pop연산이 많은 경우 deque를 collection에서 받아와서 쓰자