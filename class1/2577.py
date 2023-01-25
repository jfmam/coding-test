import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())

s = list(str(a * b * c))
arr = [0 for _ in range(10)]
for i in s:
    arr[int(i)] += 1

for i in arr:
    print(i)