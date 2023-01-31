import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())
s = 0
while n != 0:
    d = 2 ** (n-1)
    a,b = r // d, c// d
    if a == 0 and b == 0:
        s += 0
    elif a == 0 and b == 1:
        s += (d * d)
    elif a == 1 and b == 0:
        s += (d * d) * 2
    elif a == 1 and b == 1:
        s += (d * d) * 3
    r = r % d
    c = c % d
    n -= 1

print(s)
