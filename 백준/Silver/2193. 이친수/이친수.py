n = int(input())

d = [[0] * 2 for _ in range(91)]
d[1][0],d[1][1] = 0,1
d[2][0],d[2][1] = 1,0

if n <= 2:
    print(1)
else:
    for i in range(3, n+1):
        d[i][0] = d[i-1][0] + d[i-2][0]
        d[i][1] = d[i-1][1] + d[i-2][1]
    print(sum(d[n]))