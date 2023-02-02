import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
a = set([])
if m != 0:
    a = set(input().split())
ans = abs(100 - n)

for i in range(1000001): # 최댓값이 50만인 것을 상정하였을 때 제일큰 최솟값은 0이있기 때문에 -50만이 된다. 그래서 1000001을 최댓값으로 잡는다.
    i = str(i)
    for j in range(len(i)):
        if int(i[j]) in a: # in을통해 리스트의 값이 포함되어있는지 확인 할 수 있다. a가 str형태여도 사용가능하다.
            break
        elif j == len(i) -1: # 끝까지 도달했다면 min갱신
            ans = min(ans, len(i) + abs(int(i)-n))
print(ans)