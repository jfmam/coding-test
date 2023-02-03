# 1927
import heapq
import sys
heap = []

n = int(input())
for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        # heapq.heappush(heap, num) # 기존방법은 최소 힙
        heapq.heappush(heap, (-num, num)) # (우선순위, 배열에 저장 되는 실제 값) -> -를 붙여 순서를 뒤집는다(최대힙)
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
