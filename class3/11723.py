import sys
input = sys.stdin.readline

n = int(input())
a = {}
# res = []
for _ in range(n):
    b = input().split()
    if len(b) == 1:
        if b[0] == "all":  # split은 배열의 형태로 나온다
            for i in range(1, 21):
                a[i] = i
        elif b[0] == "empty":
            a.clear()
    else:
        c = int(b[1])
        b = b[0]
        if b == "add":
            a[c] = c
        elif b == "remove":
            if a.get(c):
                del a[c]
        elif b == "check":
            print(1 if a.get(c) else 0)
        elif b == "toggle":
            if a.get(c):
                del a[c]
            else:
                a[c] = c

# print(*res, sep="\n")
