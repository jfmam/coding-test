import sys
input = sys.stdin.readline

n,m= map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = max(a)
Max = -99999999

# mid가 의미하는 것은 톱의 길이, 톱의길이가 어느경우에 더 짧아지고 길어져야 하는가를 생각하면 lt rt 이동에 대해서 판별할 수 있다.
while lt <= rt:
    mid = (lt + rt) // 2
    b = [i - mid if i > mid else 0 for i in a]
    s = sum(b)
    if s > m:
        Max = max(Max, mid)
        lt = mid + 1 
    elif s < m:
        rt = mid - 1
    else:
        Max = max(Max, mid)
        lt = mid + 1

print(Max)
    