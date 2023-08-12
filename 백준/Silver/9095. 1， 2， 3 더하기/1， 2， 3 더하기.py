import sys
n = int(input())
answer = []
for _ in range(n):
    k = int(input())
    d = [0] * 12
    d[1] = 1
    d[2] = 2
    d[3] = 4
    if k <= 3:
        answer.append(d[k])
    else:
        for i in range(4, k+1):
            d[i] = d[i-3] + d[i-1] + d[i-2]
        answer.append(d[k])

for i in answer:
    print(i)