import sys
import heapq
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)
a.sort(key = lambda x: x[1]) # day를 기준으로 sort
p_list = []

for i in a:
    p,d = i
    heapq.heappush(p_list, p)
    if(len(p_list) > d):
        heapq.heappop(p_list)
print(sum(p_list))