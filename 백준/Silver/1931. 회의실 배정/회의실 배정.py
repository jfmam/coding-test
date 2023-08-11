import sys
input = sys.stdin.readline
n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
a.sort(key=lambda x: (x[1], x[0]))
cur = 0
j = 1
cnt = 1
while cur < n and j < n:
    sc,ec = a[cur]
    sj,ej = a[j]
    if ec <= sj:
        cur = j
        cnt += 1
    j+= 1
print(cnt)