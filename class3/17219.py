import sys
input = sys.stdin.readline

n,m = map(int, input().split())
a = {}

for _ in range(n):
    b,c = input().rstrip().split()
    a[b] = c
for _ in range(m):
    d = input().rstrip()
    print(a[d])