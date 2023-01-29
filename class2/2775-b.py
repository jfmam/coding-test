import sys
input = sys.stdin.readline
test = int(input().rstrip())

for i in range(test):
    k = int(input().rstrip())
    n = int(input().rstrip())

    a = [i for i in range(n+1)]
    
    for i in range(k):
        for j in range(n):
            a[j] += a[j+1] # 옆집 + 아랫집이 갖는 의미는 a[j-1] + a[j]과 같다. j-1은 이미 갱신된 값임으로 옆집을 의미한다
    print(a[-1])