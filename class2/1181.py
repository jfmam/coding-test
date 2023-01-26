import sys
input = sys.stdin.readline
n = int(input())
a = {}
for _ in range(n):
    temp = input().rstrip()
    if not a.get(temp):
        a[temp] = len(temp)
arr = sorted(a.items(), key=lambda x:(x[1], x[0]))
res = list(map(lambda x:x[0], arr))
print(*res, end="\n")