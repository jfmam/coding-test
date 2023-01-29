import sys
input = sys.stdin.readline
n = int(input().rstrip())
ans = 0

for i in range(n):
    a = list(map(int, str(i)))
    s = i + sum(a)
    if s == n:
        ans = i
        break
    
print(ans)