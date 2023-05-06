import sys
input = sys.stdin.readline

n, m = map(int, input().split())
knowList = set(input().split()[1:])
parties = []

for _ in range(m):
    parties.append(set(input().split()[1:]))

# knowlist를 모두 구한다음
cnt = 0
for _ in range(m):
    for party in parties:
        if party & knowList:
            knowList = knowList.union(party)

# know리스트에 없는 파티만 구한다.
for party in parties:
    if party & knowList:
        continue
    cnt += 1

print(cnt)
