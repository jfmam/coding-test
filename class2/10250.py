import sys
input = sys.stdin.readline
test = int(input())

res = []
for i in range(test):
    h,w,n = map(int, input().split())
    
    ho = n % h
    ch = (n // h) +1
    if ho == 0:
        ch = n // h
        ho = h
    res.append(str(ho)+str(ch).zfill(2))
print(*res, sep="\n")