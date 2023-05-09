# 순서대로 먼저 어떻게 고를 것인가?
#
import sys
input = sys.stdin.readline

L, C = map(int, input().split())
a = sorted(input().rstrip().split())
ch = [0] * C
answer = set([])


def dfs(s, cnt, st):
    global answer
    if cnt == L:
        j = 0
        m = 0
        for i in s:
            if i in ['a', 'e', 'i', 'o', 'u']:
                m += 1
            else:
                j += 1
        if j >= 2 and m >= 1:
            answer.add("".join(sorted(s)))
    for i in range(st, C):
        if ch[i] == 0:
            ch[i] = 1
            dfs(s + a[i], cnt + 1, st + 1)
            ch[i] = 0


dfs('', 0, 0)
for i in answer:
    print(i)
