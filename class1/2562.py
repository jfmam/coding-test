import sys
input = sys.stdin.readline
a = []
for _ in range(9):
    a.append(int(input()))
m = max(a)
idx = a.index(m)

print(m)
print(idx+1)