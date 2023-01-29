import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = []
for _ in range(n):
    a.append(int(input().rstrip()))
print(*sorted(a), sep="\n")