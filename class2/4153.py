import sys
input = sys.stdin.readline
res = []

while True:
    ar = sorted(list(map(int, input().split())))
    a = ar[0]
    b = ar[1]
    c = ar[2]

    if a == 0 and b == 0 and c == 0:
        break
    s = (a ** 2) + (b ** 2)
    res.append('right') if s == (c**2) else res.append('wrong')

print(*res, sep="\n")
