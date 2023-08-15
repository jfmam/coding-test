import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
target = []
for _ in range(n):
    a.append(list(map(int, input().strip())))
for _ in range(n):
    target.append(list(map(int, input().strip())))
answer = 0

if n < 3 or m < 3:
    if a == target:
        print(0)  # 입력된 행렬이 이미 같은 경우
    else:
        print(-1)  # 불가능한 경우
    exit(0)

for i in range(n-2):
    for j in range(m-2):
        if a[i][j] == target[i][j]:
            continue
        
        for k in range(i, i+3):
            for l in range(j, j+3):
                a[k][l] = 1 - a[k][l]
        answer += 1

if a == target:
    print(answer)
else:
    print(-1)
