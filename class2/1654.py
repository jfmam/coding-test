import sys
import math
input = sys.stdin.readline
k,n = map(int, input().split())
a = []
for _ in range(k):
    a.append(int(input()))

lt = 1
# 줄을 안쓰고 버리는 경우도 있기 때문에 rt는 큰 수로 잡아야 한다
rt = max(a) 
Max = -1

# 길이를 기준으로 이분탐색 진행
while rt >= lt:
    mid = int((lt + rt) / 2)
    s = 0
    for i in a:
        s += math.floor(i / mid)
    if s < n:
        rt = mid - 1
    elif s >= n:
        Max = max(mid, Max)
        lt = mid + 1
print(Max)

# 개수를 기준으로 이분탐색을 진행
# while (lt <= rt):
#     mid = (lt + rt) // 2
#     cnt = 0
#     for i in range(k):
#         cnt += (a[i] // mid)
#     if cnt >= n:
#         더 크게 잘라서 갯수를 줄이고 최대길이를 늘린다
#         start = mid + 1
#     else:
#           더 작게 잘라서 갯수를 늘리고 최대길이를 줄린다. 
#         end = mid - 1
