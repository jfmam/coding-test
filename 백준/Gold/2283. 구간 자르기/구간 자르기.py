import sys
input = sys.stdin.readline
n,k = map(int, input().split())
a = []

max_len = 0
vertical = [0] * 1000001
for _ in range(n):
    start,end = map(int, input().split())
    max_len = max(max_len, end)
    for i in range(start,end):
        vertical[i] += 1 # 수직선으로 자를 때 해당구간이 얼마나 겹치는지 확인
    
s,e = 0,0
Sum = 0
answer = [0,0]
while s <= e and e <= max_len: #
    if Sum == k:
        answer = [s,e]
        break
    elif Sum < k:
        Sum += vertical[e] # 겹치는 만큼 더하기
        e += 1
    else:
        Sum -= vertical[s] # 겹치는 만큼 빼기
        s += 1
print(answer[0], answer[1], sep=" ")