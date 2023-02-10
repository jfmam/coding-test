import math

n = int(input())
dp = [0, 1]

for i in range(2, n+1): # 2부터 만들어 나가기 -> dp[i]를 만들면서 n까지 가는 bottom up 형태
    minValue = 1e9
    for j in range(1, int(math.sqrt(i)) + 1): # i 보다 작은 제곱수들을 뺀 값 도달
        minValue = min(minValue, dp[i - j**2]) # 최소 개수 구하기
    dp.append(minValue + 1) # + 1을 해줌으로써 최소 개수 완성

print(dp[n])
