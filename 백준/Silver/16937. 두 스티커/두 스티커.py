import sys

h, w = map(int, input().split())
n = int(input())
a = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))

result = 0
for i in range(n):
    for j in range(i + 1, n):
        # 두개 선택
        r1, c1 = a[i] 
        r2, c2 = a[j]
        
        # 회전안한 경우 세로로 이어붙였을 때 or 가로로 이어 붙였을 때
        if (r1 + r2 <= h and max(c1, c2) <= w) or (max(r1, r2) <= h and c1 + c2 <= w):
            result = max(result, r1*c1 + r2*c2)
        # r1,c1을 90도 회전, 세로로 이버 붙일때, 가로로 이어 붙일 때
        if (c1 + r2 <= h and max(r1, c2) <= w) or (max(c1, r2) <= h and r1 + c2 <= w):
            result = max(result, r1*c1 + r2*c2)
        # r2,c2,회전, 반복
        if (c1 + c2 <= h and max(r1, r2) <= w) or (max(c1, c2) <= h and r1 + r2 <= w):
            result = max(result, r1*c1 + r2*c2)
        # 둘다회전
        if (r1 + c2 <= h and max(c1, r2) <= w) or (max(r1, c2) <= h and c1 + r2 <= w):
            result = max(result, r1*c1 + r2*c2)

print(result)