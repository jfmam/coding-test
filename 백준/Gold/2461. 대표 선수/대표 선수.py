import sys
import heapq
input = sys.stdin.readline
n,m = map(int, input().split())
a = []
hq = []
maxVal = 0
pointer = [0] * (n)
for i in range(n):
    tmp = list(map(int, input().split()))
    tmp.sort()
    maxVal = max(maxVal, tmp[0])
    a.append(tmp)
    heapq.heappush(hq, (a[i][0], i))
    
res = 10 ** 9
while hq:
    front = heapq.heappop(hq)
    minVal = front[0]
    min_index = front[1]
    
    res = min(res, maxVal - minVal)
    if pointer[min_index] == m:
        break
    heapq.heappush(hq, (a[min_index][pointer[min_index]], min_index))
    maxVal = max(maxVal, a[min_index][pointer[min_index]])
    pointer[min_index] += 1
print(res)

