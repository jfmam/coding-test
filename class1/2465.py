import sys
input = sys.stdin.readline
a = list(map(lambda x: pow(int(x),2), input().split()))
res = sum(a) % 10
print(res)