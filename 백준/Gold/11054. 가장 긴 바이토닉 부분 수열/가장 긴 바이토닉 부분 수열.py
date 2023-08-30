import sys
input = sys.stdin.readline
n = int(input())
a =list(map(int,input().split()))
k = max(a)
k_idx = a.index(k)
d1 = [0] * (n)
d2 = [0] * (n)

for i in range(n):
    d1[i] = 1
    for j in range(i):
        if a[i] > a[j]:
            d1[i] = max(d1[i], d1[j] + 1)
for i in range(n-1,-1,-1):
    d2[i] = 1
    for j in range(i,n):
        if a[i] > a[j]:
            d2[i] = max(d2[i], d2[j] + 1)
s = float('-inf')
for i in range(n):
    s = max(s, d1[i] + d2[i] - 1)
print(s)
    
           