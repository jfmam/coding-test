import sys
input = sys.stdin.readline
N = int(input())
snow = list(map(int,input().split()))
snow.sort()
diff = 4000000001
for i in range(N-3):
    for j in range(i+3, N):
        fix = snow[i] + snow[j]
        left, right = i+1, j-1
 
        while left < right:
            s = snow[left] + snow[right]
            if abs(s - fix) < diff:
                diff = abs(s - fix)
            
            if s < fix:
                left += 1
            elif s > fix:
                right -= 1
            else:
                print(0)
                sys.exit(0)
 
print(diff)