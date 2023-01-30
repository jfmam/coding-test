import sys
input = sys.stdin.readline
n = int(input().rstrip())
a = []
for _ in range(n):
    b, c = map(int, input().split())
    a.append((b, c))
res = [1 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            res[i] += 1
print(*res)

# 공동등수를 표시하는 방법
# 자기보다 등수가 더 높은 사람을 만나면 +1을 해줌으로써 공동 등수를 표시하기가 쉬워진다.