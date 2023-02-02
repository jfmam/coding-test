import sys
input = sys.stdin.readline
a = input().rstrip().split("-") # -를 기준으로 나누어서 0번째인덱스 value에서 나머지 인덱스의 value를 뺴줌으로써 구할 수 있다.
b = []
for i in a:
    tmp = list(map(int, i.split("+"))) # 문자열로 +가 포함되어있기 때문에 +에서 split하여 전부 구해준다.
    b.append(sum(tmp))
s = b.pop(0)
if b:
    for i in b:
        s -= i
print(s)