import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
maxValue = max(a)
b = [i / maxValue*100 for i in a]
res = sum(b) / n
print(res)