import sys
import heapq
input = sys.stdin.readline


test = int(input())
for _ in range(test):
    max_heap, min_heap = [], []
    visit = [False] * 1_000_001

    order_num = int(input())

    for key in range(order_num):
        order = input().rsplit()
        if order[0] == 'I':
            heapq.heappush(min_heap, (int(order[1]), key)) # (우선순위, value)
            heapq.heappush(max_heap, (int(order[1]) * -1, key))
            visit[key] = True  # True이면 어떤 힙에서도 아직 삭제되지 않은 상태

        elif order[0] == 'D':
            # 최소 힙 제거
            if order[1] == '-1':
                while min_heap and not visit[min_heap[0][1]]:
                    # if visit[min_heap[0][1]]: #이미 방문한 min heap가 없어질때까지
                        heapq.heappop(min_heap)  # 1. 먼저 while 문을 돌면서 이미 방문한 경우 삭제
                        # 탈출문: visit[min_heap[0][1]] = False인게 없으면 탈출 한다.
                    # flag =False
                    # for i in visit:
                    #     if not i:
                    #         flag = True
                    # if flag:
                    #     break
                if min_heap:
                    # 2. 최소 힙이 있으면 제거
                    visit[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            elif order[1] == '1':
                # 1번과 동일
                while max_heap and not visit[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

# while문 탈출 후 최소힙 pop으로 끝났을 경우 -> 최대힙 visit한 노드들을 pop 해주어야 한다
# 최대힙도 동일하다.
    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
