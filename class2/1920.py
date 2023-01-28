import sys
input = sys.stdin.readline
n = int(input().rstrip())
a = set(map(int, input().split()))
print(a)
m = int(input().rstrip())
b = list(map(int, input().split()))
res = []

# for i in b:
    # print(1) if i in a else print(0) # True실행문 if 조건문 else false 실행문

for i in b:
    lt, rt = 0, n-1
    flag = False
    while lt <= rt:
        mid = (lt + rt) // 2 #mid 위치 중요!
        if i < a[mid]:
            rt = mid - 1
        elif i > a[mid]:
            lt = mid + 1
        else:
            res.append(1)
            flag = True
            break
    if not flag:
        res.append(0)
for i in res:
    print(i)