import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
a = set([])
if m != 0:
    a = set(input().split())
ans = abs(100 - n)

for i in range(1000001):
    for j in str(i):
        if j in a:
            break
    else:
        ans = min(ans, len(str(i)) + abs(i-n))
print(ans)