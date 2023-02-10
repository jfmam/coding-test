import sys
input = sys.stdin.readline
n = int(input())

b = {}
a = list(map(int, input().split()))

c = sorted(set(a))
# set은 iterable 하며 for 문으로 접근 가능
# sorted 함수를 사용하여 set 배열 정렬 가능

cnt = 0
for i in c:
    b[i] = cnt
    cnt += 1
for i in a:
    print(b[i],sep=" ", end=" ")

# 1. 공동 등수 문제로 접근하려 했으나 숫자가 겹치는 경우가 있어서 set함수로 먼저 겹치는 부분을 제거 한 후 dict에 [index] = count 값으로 저장
# 2. a 리스트 순회하면서 dict에 있는 값을 꺼내 출력한다