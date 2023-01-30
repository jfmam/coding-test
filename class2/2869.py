import sys
import math
input = sys.stdin.readline
a, b, v = map(int, input().split())
cnt = 1

if a != v:
    tmp = (v-a) / (a-b)
    cnt += math.ceil(tmp)  # 3.0을 올림하면 3.0이기 떄문에 상관없다

print(int(cnt))
