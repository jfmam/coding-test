import sys
from collections import defaultdict
input = sys.stdin.readline
n,k = map(int, input().split())
a = list(map(int, input().split()))

s,e=0,0
counter = defaultdict(int)
Max = 0
while s < n and e < n:
    if counter[a[e]] < k:
        counter[a[e]] += 1
        e += 1
    else:
        counter[a[s]] -= 1
        s += 1
    Max = max(Max, e-s)

print(Max)
    