import sys

input = sys.stdin.readline

n, l, r, x = map(int, input().split())
a = list(map(int, input().split()))

def dfs(idx, num, selected):
    count = 0

    if idx == num:
        s = sum(selected)
        ss = sorted(selected)
        if l <= s <= r and ss[-1] - ss[0] >= x:
            return 1
        return 0

    for i in range(idx, n):
        selected.append(a[i])
        count += dfs(i + 1, num, selected)
        selected.pop()

    return count

answer = 0

for i in range(2, n+1):
    answer += dfs(0, i, [])

print(answer)
