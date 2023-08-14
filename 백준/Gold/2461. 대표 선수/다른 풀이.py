# 파이썬에서는 시간초과 발생

import sys
input = sys.stdin.readline
n,m = map(int, input().split())
a = []
pointer = [0] * (n)
for _ in range(n):
    tmp = list(map(int, input().split()))
    a.append(sorted(tmp))
answer = float('inf')
while True:
    Max = float('-inf')
    min_index, Min = -1, float('inf')
    for i in range(n):
        if Max < a[i][pointer[i]]:
            Max = a[i][pointer[i]]
        if Min > a[i][pointer[i]]:
            Min = a[i][pointer[i]]
            min_index = i
    if (Max - Min) < answer:
        answer = Max-Min
    pointer[min_index] += 1
    if pointer[min_index] >= m:
        print(answer)
        break

