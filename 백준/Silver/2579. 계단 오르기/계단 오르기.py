import sys
input = sys.stdin.readline
n = int(input())
a = [0]
for _ in range(n):
    a.append(int(input()))
if n == 1:
    print(a[1])
    exit()
ch = [0] * (n+1)
ch[1] = a[1]
ch[2] = a[1] + a[2]
if n==2:
    print(ch[2])
    exit()
ch[3] = max(a[1]+a[3],a[2]+a[3])
if n == 3:
    print(ch[n])
else:
    for i in range(4, n+1):
        ch[i] = max(ch[i-3]+a[i-1]+a[i], ch[i-2]+a[i])
    print(ch[n])