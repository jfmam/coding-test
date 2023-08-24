n,k = map(int, input().split()) # n은 수 k는 갯수
d = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1):
    d[i][1] = 1
for i in range(2, k+1):
    d[1][i] = i
for i in range(2,n+1):
    for j in range(1,k+1):
        d[i][j] = (d[i-1][j] + d[i][j-1]) % 1000000000
print(d[n][k] % 1000000000)
        