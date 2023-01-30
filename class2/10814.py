import sys
input = sys.stdin.readline

n = int(input())
res = []
for _ in range(n):
    a, b = input().split()
    res.append((int(a), b))

res = sorted(res, key=lambda x: x[0])
for i in res:
    print("{} {}".format(i[0], i[1]), end='\n')
