import sys
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    n,m = map(int, input().split())
    a.append((n,m))
res = sorted(a, key=lambda x: (x[1], x[0]))

for i in res:
    print("{} {}".format(i[0],i[1]), end="\n")