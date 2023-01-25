import sys
input = sys.stdin.readline
n = int(input())
res = []

def solution(s):
    acc = 0
    point = 0
    for i in list(s):
        if i=='O':
            acc += 1
            point += acc
        else:
            acc = 0
    return point
for i in range(n):
    a = input()
    res.append(solution(a))
print(*res, sep="\n")