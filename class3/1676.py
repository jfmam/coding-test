from functools import reduce
n = int(input())

a = reduce(lambda a, b: a*b, [i for i in range(1, n+1)], 1) # initial value를 적지않으면 0일 때 리스트타입에러 반환,
# 원래는 [0]을 초기값으로 받는데 아무것도 없어서 에러남

cnt = 0
while a % 10 == 0:
    cnt += 1
    a = a//10
print(cnt)