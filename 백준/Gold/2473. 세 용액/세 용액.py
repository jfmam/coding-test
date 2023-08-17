import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
answer = [0, 0, 0]
min_diff = float('inf')

for i in range(n - 2):
    left, right = i + 1, n - 1
    while left < right:
        total = a[i] + a[left] + a[right]
        diff = abs(total)
        
        if diff < min_diff:
            min_diff = diff
            answer = [a[i], a[left], a[right]]
        
        if total < 0:
            left += 1
        else:
            right -= 1

print(*answer, sep=" ")
