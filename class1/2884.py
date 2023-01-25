import sys
input = sys.stdin.readline
h, m = map(int, input().split())

global a
global b
if m - 45 < 0:
    b = m + 60 - 45
    if h == 0:
        a = 23
    else:
        a = h-1
else:
    a = h
    b = m - 45
print(a, b, sep=" ")
