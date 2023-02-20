import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ch = [0] * (n+1)
a = list(map(int, input().split()))
if len(a) != 1:
    a.pop(0)
    for i in a:
        ch[i] += 1


b = []
for _ in range(m):
    b = list(map(int, input().split()))
    b.pop(0)
    for j in b:
        ch[j] += 1
cnt = 0
for i in range(n+1):
    if ch[i] == 1:
       cnt += 1
print(cnt)
