import sys
input = sys.stdin.readline
n = int(input().rstrip())
a = []
for _ in range(n):
    a.append(input().rstrip())

res = []
for i in a:
    b = list(i)
    if len(b) % 2 != 0:
        res.append("NO")
        continue
    stk = []
    for j in b:
        if len(stk) == 0:
            stk.append(j)
            continue
        if stk[-1] == "(" and j == ")":
            stk.pop()
        else:
            stk.append(j)
    if len(stk) == 0:
        res.append("YES")
    else:
        res.append("NO")
print(*res, sep="\n")