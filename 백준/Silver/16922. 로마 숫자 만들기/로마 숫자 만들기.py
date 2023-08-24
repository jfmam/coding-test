import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
n = int(input())
# I, V, X, L을 사용한다. 각 문자는 1, 5, 10, 50
a = [1,5,10,50]
answer = set([])

def dfs(idx,s, start):
    if idx == n:
        answer.add(s)
        return
    else:
        for i in range(start, len(a)):
            dfs(idx+1, s + a[i], i)
dfs(0,0,0)
print(len(answer))
        