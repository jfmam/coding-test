import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
Max = max(a)
m = Max
cnt = 0
ch = [True for _ in range(m + 1)]
ch[0] = False
ch[1] = False

for i in range(2, m + 1):
    j = 2
    while i * j <= m:
        ch[i*j] = False
        j += 1
for i in a:
    if ch[i]:
        cnt += 1
print(cnt)