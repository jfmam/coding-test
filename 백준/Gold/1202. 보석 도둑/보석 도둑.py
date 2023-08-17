import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())
jewelry = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
jewelry.sort()
bags.sort()
tmp = []
result = 0
for bag in bags:
    while jewelry and bag >= jewelry[0][0]: # bag가 보석보다 작을 때만 반복문
        heapq.heappush(tmp, -jewelry[0][1]) # 보석의 가격을 기준으로 내림차순으로 저장한다. 최대힙
        heapq.heappop(jewelry) # 기존 보석은 pop
    
    if tmp: # 가방에 들어갈 수 있는 보석 중 제일 비싼 것을 result에 더해준다.
        result += heapq.heappop(tmp)
    elif not jewelry: # 만약 없을 경우 for문을 멈춘다.
        break

print(-result) # 최대힙으로 했음으로 -1을 곱해준다.