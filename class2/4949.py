import sys
input = sys.stdin.readline
a = []
while True:
    b = input()
    if(b[0] == '.'):
        break

    j = 0
    temp = []
    while b[j] != '.':
        if b[j] == '(' or b[j] == '[' or b[j] == ')' or b[j] == ']':
            temp.append(b[j])
        j += 1
    a.append(temp)

res = []
for i in a:
    if len(i) == 0:
        res.append("yes")
        continue
    if len(i) % 2 != 0:
        res.append("no")
        continue
    stk = []
    for j in i:
        if len(stk) == 0:
            stk.append(j)
            continue
        if stk[-1] == "(" and j == ")":
            stk.pop()
        elif stk[-1] == "[" and j == "]":
            stk.pop()
        else:
            stk.append(j)
    if len(stk) == 0:
        res.append("yes")
    else:
        res.append("no")

print(*res, sep="\n")
