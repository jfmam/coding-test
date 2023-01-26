import sys
input = sys.stdin.readline

x,y,w,h = map(int, input().split())
res = [x,y, w-x, h-y]
res.sort()

print(res[0])
