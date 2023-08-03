import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
result = 0
start,end = 0,0
ch = [False] * 100001

while start< n and end < n: # start와 end가 모두 마지막을 가르킬때까지 진행
    if not ch[a[end]]:
        ch[a[end]] = True
        end += 1
        result += (end-start)
    else:
        ch[a[start]] = False
        start += 1
print(result)
    