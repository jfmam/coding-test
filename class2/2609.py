import sys

a, b = map(int, sys.stdin.readline().split())


def gcd(a, b):  # a는 b보다 크다는 조건이 있다
    while b != 0:  # 0이 나올 떄 까지 반복
        a = a % b  # a > b 일때 나머지
        a, b = b, a  # 나머지값과 작은수를 바꾼다
    return a  # b가 0이될 때 최대공략수 a가 나온다


def lcm(a, b, g):
    return a*b // g

Max = max(a,b)
Min = min(a,b)
g = gcd(a,b)
print(g, lcm(a,b,g), end="\n")