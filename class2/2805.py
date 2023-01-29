import sys
input = sys.stdin.readline

n,m= map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = max(a)
Max = -99999999

while lt <= rt:
    mid = (lt + rt) // 2
    b = [i - mid if i > mid else 0 for i in a]
    s = sum(b)
    if s > m:
        Max = max(Max, mid)
        lt = mid + 1
    elif s < m:
        rt = mid - 1
    else:
        Max = max(Max, mid)
        lt = mid + 1

print(Max)
    