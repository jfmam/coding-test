import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)
a.sort(key=lambda x: (-x[0], x[1]))  # 먼저 점수 높은 것을 고려하도록 순서 변경
q = deque(a)
answer = 0
ch = defaultdict(int)

while q:
    p, d = q.popleft()
    while ch[d]:  # 이미 해당 날짜에 선택된 경우에는 날짜를 감소시키며 빈 슬롯 찾기
        d -= 1
    if d >= 1:  # 선택된 날짜가 1 이상이어야 강연이 가능
        answer += p
        ch[d] = 1

print(answer)
