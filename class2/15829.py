import sys
input = sys.stdin.readline
n = int(input())
a = input().rstrip()


def findAlpha(ch: chr):
    return ord(ch) - 96


cnt = 0
s = 0
for i in list(a):
    b = findAlpha(i)
    s += (b*(31**cnt))
    cnt += 1
print(s % 1234567891)
