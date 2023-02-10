import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
res = []
b = [0]
cnt = 0
for i in a:
    cnt += i
    b.append(cnt) # 누적값 저장하기

for i in range(m):
    c,d = map(int, input().split())
    res.append(b[d] - b[c-1]) # 누적값에서 제외해야 될값
    
print(*res, sep="\n")

# prefix_sum 누적값 구하기