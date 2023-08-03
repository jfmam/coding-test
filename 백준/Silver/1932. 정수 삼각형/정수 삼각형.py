import sys
input = sys.stdin.readline
n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

dp = [[0] * (i+1) for i in range(n)]  # dp 배열 크기 수정

dp[0][0] = a[0][0]

if n == 1:
    print(dp[0][0])
    exit(0)

for i in range(1, n):  # i=0인 경우는 위에서 처리되었으므로 1부터 시작
    dp[i][0] = dp[i-1][0] + a[i][0]  # 각 삼각형 왼쪽 끝 값 갱신
    dp[i][i] = dp[i-1][i-1] + a[i][i]  # 각 삼각형 오른쪽 끝 값 갱신
    for j in range(1, i):  # 중간 값들 갱신
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + a[i][j]

print(max(dp[n-1]))
