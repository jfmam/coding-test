import sys
input = sys.stdin.readline

c = int(input())
sol = []


def solution(n, s):
    arr = list(s)
    res = ""
    for i in arr:
        res += (i * n)
    return res


for i in range(c):
    a, b = input().split()
    sol.append(solution(int(a), b))

print(*sol, end="\n")  # arr *을 붙여 대괄호 없이 출력한다.
