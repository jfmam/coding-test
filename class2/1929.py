from math import sqrt
import sys

input = sys.stdin.readline
m,n = map(int, input().split())


a = {}
for i in range(m,n+1):
    a[i] = True

for i in range(m, int(sqrt(n)) + 1): # n의 제곱근까지만 해도 된다
    if a[i] == True:
        j = 2
        while i * j <= n:
            a[i*j] = False
            j+=1
for i in range(m,n+1):
    if a[i]:
        print(i)